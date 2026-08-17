from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Any


SKILL_LINE_RE = re.compile(r"^\s*([^\s：:]{1,8})[：:]\s*(.+)$", re.MULTILINE)
PLACEHOLDER_RE = re.compile(r"【\s*(?:牌名|某牌)?\s*】")
GENERIC_PLACEHOLDER_RE = re.compile(r"【(?:某|待定|TODO|TBD)[^】]*】", re.IGNORECASE)
NON_SKILL_LABELS = {
    "设计说明",
    "可调参数",
    "衍生牌/对象名",
    "当前结论",
    "当前方案",
    "联动关系",
    "待确认",
}


@dataclass(frozen=True)
class Finding:
    rule_id: str
    severity: str
    message: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "rule_id": self.rule_id,
            "severity": self.severity,
            "message": self.message,
        }


def _bracket_balance(text: str, opening: str, closing: str) -> bool:
    depth = 0
    for character in text:
        if character == opening:
            depth += 1
        elif character == closing:
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


def lint_text(text: str, full_group: bool = False) -> list[Finding]:
    findings: list[Finding] = []

    if PLACEHOLDER_RE.search(text) or GENERIC_PLACEHOLDER_RE.search(text):
        findings.append(Finding("SG001", "error", "存在空白或占位牌名。"))

    if not _bracket_balance(text, "【", "】"):
        findings.append(Finding("SG002", "error", "牌名方头括号不成对。"))

    if not _bracket_balance(text, "（", "）"):
        findings.append(Finding("SG003", "error", "中文圆括号不成对。"))

    skill_names = [
        match.group(1)
        for match in SKILL_LINE_RE.finditer(text)
        if match.group(1) not in NON_SKILL_LABELS
    ]
    duplicate_names = sorted({name for name in skill_names if skill_names.count(name) > 1})
    if duplicate_names:
        findings.append(
            Finding("SG004", "error", f"存在重复技能名：{'、'.join(duplicate_names)}。")
        )

    if full_group and skill_names and not 2 <= len(skill_names) <= 4:
        findings.append(
            Finding("SG005", "warning", f"识别到{len(skill_names)}个技能；通常应为2至4个。")
        )

    if "立即" in text:
        findings.append(Finding("SG006", "warning", "出现“立即”；应改用明确事件时机。"))

    if "每当" in text:
        findings.append(Finding("SG007", "warning", "出现“每当”；应确认是否可改为明确的“当……时/后”。"))

    if "视为使用" in text and re.search(r"将[^。；\n]{0,24}牌当", text):
        findings.append(
            Finding("SG008", "info", "同一文本同时出现虚拟牌和转化牌表述，请分别检查材料、牌面信息和移动。")
        )

    if re.search(r"视为使用[^。；\n]{0,40}【(?:桃|酒)】", text):
        findings.append(
            Finding("SG009", "warning", "存在虚拟使用【桃】或【酒】的路径，应检查生存牌复制压力。")
        )

    if "出牌阶段限一次" in text and "无懈可击" in text:
        findings.append(
            Finding("SG010", "info", "出牌阶段主动技涉及【无懈可击】，请确认空闲时间点与响应窗口没有混用。")
        )

    return findings


def findings_as_dict(findings: list[Finding]) -> dict[str, Any]:
    counts = {
        severity: sum(1 for finding in findings if finding.severity == severity)
        for severity in ("error", "warning", "info")
    }
    return {
        "protocol_version": 1,
        "ok": counts["error"] == 0,
        "counts": counts,
        "findings": [finding.as_dict() for finding in findings],
    }


def findings_as_markdown(findings: list[Finding]) -> str:
    result = findings_as_dict(findings)
    lines = [
        "# Sanguosha Skill Lint",
        "",
        f"- Result: `{'pass' if result['ok'] else 'fail'}`",
        f"- Errors: `{result['counts']['error']}`",
        f"- Warnings: `{result['counts']['warning']}`",
        f"- Info: `{result['counts']['info']}`",
    ]
    if findings:
        lines.extend(["", "## Findings", ""])
        for finding in findings:
            lines.append(f"- **{finding.severity.upper()} {finding.rule_id}**: {finding.message}")
    return "\n".join(lines).rstrip() + "\n"
