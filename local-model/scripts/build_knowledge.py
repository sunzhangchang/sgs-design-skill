from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = Path(__file__).resolve().parents[1] / "knowledge"


def normalize(text: str) -> str:
    text = text.replace("\r\n", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def main() -> None:
    source_files = [ROOT / "SKILL.md"]
    source_files.extend(sorted((ROOT / "references").rglob("*.md")))
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for old_file in OUTPUT.glob("*.txt"):
        old_file.unlink()
    for source in source_files:
        if source.is_file():
            relative = source.relative_to(ROOT).as_posix().replace("/", "__")
            (OUTPUT / f"{relative}.txt").write_text(normalize(source.read_text(encoding="utf-8")), encoding="utf-8")
    print(f"wrote {len(source_files)} knowledge files to {OUTPUT}")


if __name__ == "__main__":
    main()
