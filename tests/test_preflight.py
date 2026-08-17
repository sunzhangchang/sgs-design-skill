from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from contextlib import redirect_stdout
from io import StringIO
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from sgs_preflight.cli import main as cli_main
from sgs_preflight.index import SQLiteKnowledgeIndex, ensure_index, load_config
from sgs_preflight.linting import lint_text
from sgs_preflight.routing import build_context


class PreflightTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = load_config(ROOT)
        cls.state = ensure_index(ROOT, cls.config, rebuild=True)
        cls.index = SQLiteKnowledgeIndex(cls.state.database)

    def context(
        self,
        query: str,
        task: str,
        stage: str = "auto",
        max_chars: int = 12000,
        max_chunks: int = 12,
    ):
        return build_context(
            root=ROOT,
            config=self.config,
            index=self.index,
            query=query,
            requested_task=task,
            requested_stage=stage,
            max_chars=max_chars,
            max_chunks=max_chunks,
            search_chunks=6,
            index_rebuilt=False,
            index_elapsed_ms=0.0,
        )

    @staticmethod
    def keys(bundle) -> set[tuple[str, str]]:
        return {(item.chunk.path, item.chunk.heading) for item in bundle.selections}

    def test_idle_timing_route(self) -> None:
        bundle = self.context(
            "奇策能否在【无懈可击】响应窗口发动？出牌阶段限一次与空闲时间点",
            "review",
            "rules",
        )
        keys = self.keys(bundle)
        self.assertIn(("references/event-glossary.md", "Idle Timing Versus Frequency"), keys)
        self.assertIn("idle-frequency", bundle.matched_routes)
        self.assertFalse(any(path == "references/contest-evaluation.md" for path, _ in keys))

    def test_clan_support_route_avoids_approximate_noise(self) -> None:
        bundle = self.context(
            "设计太原王氏王济，宗族技中流，定位辅助且单挑有空间",
            "fresh-design",
            "play",
        )
        keys = self.keys(bundle)
        self.assertIn(("references/design-heuristics.md", "太原王氏: 中流"), keys)
        self.assertIn(("references/design-heuristics.md", "Support With Solo Play"), keys)
        self.assertFalse(any(path.startswith("references/mechanics/") for path, _ in keys))
        self.assertFalse(any(path == "references/naming-titles.md" for path, _ in keys))

    def test_virtual_card_route_is_specific(self) -> None:
        bundle = self.context(
            "检查视为使用一张明置手牌：虚拟牌与转化牌、牌名和花色点数",
            "review",
            "rules",
        )
        keys = self.keys(bundle)
        self.assertIn(("references/gamecard-operations.md", "视为"), keys)
        self.assertIn(("references/gamecard-operations.md", "将牌当A牌操作"), keys)
        self.assertIn(("references/value-glossary.md", "Card Points"), keys)
        self.assertNotIn(("references/value-glossary.md", "Distance"), keys)

    def test_intake_does_not_execute_design_routes(self) -> None:
        bundle = self.context(
            "吸收一篇新的机制评价文章，保留原文并处理冲突",
            "intake",
        )
        keys = self.keys(bundle)
        self.assertIn(("references/knowledge-intake.md", "Intake Contract"), keys)
        self.assertEqual([], bundle.matched_routes)
        self.assertFalse(any(path == "references/description-glossary.md" for path, _ in keys))

    def test_auto_classification(self) -> None:
        intake = self.context("吸收新的规则资料并保留原文", "auto", "auto")
        review = self.context("检查这个技能的时机是否合法", "auto", "auto")
        self.assertEqual("intake", intake.task)
        self.assertEqual("review", review.task)
        self.assertEqual("rules", review.stage)

    def test_budget_is_hard_and_keeps_specific_rule(self) -> None:
        bundle = self.context(
            "检查虚拟牌和时机响应窗口",
            "review",
            "rules",
            max_chars=5000,
            max_chunks=8,
        )
        self.assertLessEqual(bundle.total_chars, 5000)
        self.assertIn(("references/gamecard-operations.md", "视为"), self.keys(bundle))

    def test_linter_detects_placeholders_and_survival_virtual_card(self) -> None:
        findings = lint_text("技能：你视为使用【桃】。然后获得【】。", full_group=True)
        rule_ids = {finding.rule_id for finding in findings}
        self.assertIn("SG001", rule_ids)
        self.assertIn("SG009", rule_ids)

    def test_cli_json_protocol(self) -> None:
        output = StringIO()
        with redirect_stdout(output):
            result = cli_main(
                [
                    "--root",
                    str(ROOT),
                    "context",
                    "--task",
                    "review",
                    "--stage",
                    "rules",
                    "--query",
                    "空闲时间点",
                    "--plan-only",
                    "--format",
                    "json",
                ]
            )
        self.assertEqual(0, result)
        payload = json.loads(output.getvalue())
        self.assertEqual(1, payload["protocol_version"])
        self.assertEqual("review", payload["task"])
        self.assertTrue(payload["chunks"])

    def test_concurrent_cache_access(self) -> None:
        def open_index(_: int):
            return ensure_index(ROOT, self.config, rebuild=False)

        with ThreadPoolExecutor(max_workers=4) as executor:
            states = list(executor.map(open_index, range(8)))
        self.assertTrue(all(state.database == states[0].database for state in states))
        self.assertTrue(all(state.chunk_count == states[0].chunk_count for state in states))


if __name__ == "__main__":
    unittest.main()
