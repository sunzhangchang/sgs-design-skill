import argparse
from pathlib import Path

import yaml
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    DataCollatorForLanguageModeling,
    Trainer,
    TrainingArguments,
)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config.yaml")
    return parser.parse_args()


def main():
    args = parse_args()
    config_path = Path(args.config)
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    model_config = config["model"]
    data_config = config["data"]
    training_config = config["training"]
    lora_config = config["lora"]
    base_dir = config_path.parent

    tokenizer = AutoTokenizer.from_pretrained(model_config["name_or_path"], trust_remote_code=model_config["trust_remote_code"])
    tokenizer.pad_token = tokenizer.pad_token or tokenizer.eos_token
    quantization = BitsAndBytesConfig(
        load_in_4bit=model_config["load_in_4bit"],
        bnb_4bit_compute_dtype=getattr(__import__("torch"), model_config["compute_dtype"]),
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
    )
    model = AutoModelForCausalLM.from_pretrained(
        model_config["name_or_path"],
        quantization_config=quantization,
        device_map="auto",
        trust_remote_code=model_config["trust_remote_code"],
    )
    model = prepare_model_for_kbit_training(model)
    model = get_peft_model(model, LoraConfig(
        r=lora_config["r"],
        lora_alpha=lora_config["alpha"],
        lora_dropout=lora_config["dropout"],
        target_modules=lora_config["target_modules"],
        task_type="CAUSAL_LM",
    ))
    model.print_trainable_parameters()

    files = {"train": str(base_dir / data_config["train_file"]), "eval": str(base_dir / data_config["eval_file"])}
    dataset = load_dataset("json", data_files=files)

    def tokenize(batch):
        texts = [tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=False) for messages in batch["messages"]]
        return tokenizer(texts, truncation=True, max_length=data_config["max_seq_length"])

    tokenized = dataset.map(tokenize, batched=True, remove_columns=dataset["train"].column_names)
    output_dir = base_dir / training_config["output_dir"]
    trainer = Trainer(
        model=model,
        args=TrainingArguments(
            output_dir=str(output_dir),
            num_train_epochs=training_config["num_train_epochs"],
            per_device_train_batch_size=training_config["per_device_train_batch_size"],
            per_device_eval_batch_size=training_config["per_device_eval_batch_size"],
            gradient_accumulation_steps=training_config["gradient_accumulation_steps"],
            gradient_checkpointing=training_config["gradient_checkpointing"],
            learning_rate=training_config["learning_rate"],
            logging_steps=training_config["logging_steps"],
            save_steps=training_config["save_steps"],
            eval_steps=training_config["eval_steps"],
            eval_strategy="steps",
            save_total_limit=training_config["save_total_limit"],
            warmup_ratio=training_config["warmup_ratio"],
            max_grad_norm=training_config["max_grad_norm"],
            optim=training_config["optim"],
            report_to=training_config["report_to"],
            bf16=True,
            remove_unused_columns=False,
        ),
        train_dataset=tokenized["train"],
        eval_dataset=tokenized["eval"],
        data_collator=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False),
    )
    trainer.train()
    trainer.save_model(str(output_dir))
    tokenizer.save_pretrained(str(output_dir))


if __name__ == "__main__":
    main()
