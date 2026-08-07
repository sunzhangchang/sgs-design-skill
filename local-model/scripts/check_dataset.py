import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python scripts/check_dataset.py path/to/file.jsonl")
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"missing dataset: {path}")
        return 2
    errors = []
    count = 0
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        count += 1
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_number}: invalid JSON ({exc.msg})")
            continue
        messages = item.get("messages")
        if not isinstance(messages, list) or len(messages) < 2:
            errors.append(f"line {line_number}: messages must contain user and assistant turns")
            continue
        roles = [message.get("role") for message in messages]
        if "user" not in roles or "assistant" not in roles:
            errors.append(f"line {line_number}: missing user or assistant role")
        content = "\n".join(str(message.get("content", "")) for message in messages)
        if any(token in content for token in ("【】", "【牌名】", "【某牌】")):
            errors.append(f"line {line_number}: contains blank or placeholder card name")
    print(f"checked {count} samples: {path}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
