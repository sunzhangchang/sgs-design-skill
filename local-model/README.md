# 三国杀武将设计本地模型

这个目录提供本地模型的第一阶段骨架：知识库整理、训练数据检查、QLoRA 微调配置，以及后续本地推理的模型选择。

## 当前机器的建议

- GPU：RTX 5060 Laptop，8GB 显存
- CPU：Intel Core i7-14650HX，24 线程
- 推理首选：`Qwen/Qwen3-8B` 的 4-bit GGUF/AWQ 版本
- 训练首选：`Qwen/Qwen3-8B` 做 4-bit QLoRA
- 备用模型：`Qwen/Qwen3-4B`，适合显存不足、需要更高速度或先验证流程

不要在这台机器上做全量微调，也不要从零训练基础模型。第一阶段目标是让模型学会交互流程、设计判断和输出格式；机制资料放在检索库中维护。

## 目录

- `config.yaml`：模型、显存和训练参数
- `data/train.jsonl`：人工审核后的训练样本
- `data/eval.jsonl`：固定评测样本，不参与训练
- `knowledge/`：由 skill 文档生成的知识库文本
- `scripts/build_knowledge.py`：整理 skill 文档为可检索文本块
- `scripts/check_dataset.py`：检查 JSONL 格式、空白牌名和关键约束
- `scripts/train_qlora.py`：使用 Transformers、PEFT、bitsandbytes 进行 QLoRA

## 初始化知识库

```powershell
python scripts/build_knowledge.py
```

脚本默认从当前仓库的 `SKILL.md` 和 `references/` 读取，并写入 `knowledge/`。知识库文件不应直接当作训练问答样本。

## 准备训练数据

复制 `data/train.example.jsonl` 为 `data/train.jsonl`，逐条补充人工审核过的样本。推荐先准备 100-300 条高质量样本，覆盖：交互提问、完整设计、技能评审、失败反例。

检查数据：

```powershell
python scripts/check_dataset.py data/train.jsonl
python scripts/check_dataset.py data/eval.jsonl
```

## 安装训练依赖

建议使用 Python 3.11 的独立虚拟环境；Windows 上如果 `bitsandbytes` 或 CUDA 依赖出现兼容问题，使用 WSL2 + NVIDIA CUDA 环境。安装依赖前请先确认 PyTorch 对应你的驱动：

```powershell
pip install torch transformers datasets peft accelerate bitsandbytes pyyaml
```

运行训练：

```powershell
python scripts/train_qlora.py --config config.yaml
```

训练默认只保存 LoRA adapter，不复制完整基座模型，因此更省磁盘。模型权重、缓存和输出目录建议放在 D: 或 E:，不要放在剩余空间较少的 C:。

## 模型选择原则

- `Qwen3-8B`：质量优先，4-bit 推理适合 8GB 显存；QLoRA 需要低 batch 和短上下文。
- `Qwen3-4B`：速度和余量优先，适合作为训练调试模型。
- `Qwen3-14B`：当前显存不建议作为本地训练基座；即使量化推理也要依赖系统内存回退。

基础模型与量化文件需要从 Hugging Face 或 ModelScope 单独下载；本项目不会自动下载大文件。
