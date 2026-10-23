# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6", "jsonschema>=4.18"]
# ///
"""Replay synthetic D017 review cases; output reports observations, not approval.

Run: uv run provenance/reviews/d017_adversarial_cases.py
The cases use a reduced copy of the repository record, never modify it, and
deliberately introduce inaccurate data. They are not actual disclosure records.
"""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import tempfile

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("record_validator", ROOT / "scripts/validate_record.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def main() -> None:
    base = validator.yaml.load((ROOT / "AI_USE.yaml").read_text(encoding="utf-8"), Loader=validator.TextDateLoader)
    base["claims"] = base["claims"][:1]
    base["claims"][0]["checks"] = base["claims"][0]["checks"][:1]
    base["claims"][0]["checks"][0]["preserved_at"] = [{"note": "Synthetic review case; no evidence claim."}]

    with tempfile.TemporaryDirectory(prefix="d017-review-") as directory:
        def run(name: str, record: dict | None = None, raw: bytes | None = None) -> None:
            path = Path(directory) / f"{name}.yaml"
            if raw is None:
                raw = validator.yaml.safe_dump(record, sort_keys=False).encode("utf-8")
            path.write_bytes(raw)
            try:
                errors = validator.validate(path)
                result = {"case": name, "verdict": "FAIL" if errors else "PASS", "errors": errors}
            except Exception as error:
                # Crashes are an observation in this diagnostic, never a valid record.
                result = {"case": name, "verdict": "CRASH", "exception": type(error).__name__}
            print(json.dumps(result))

        run("control", base)
        record = copy.deepcopy(base)
        record["claims"][0]["produced_by"].append("claude")
        run("reviewer_later_contributed", record)
        record = copy.deepcopy(base)
        for system in record["participants"]["systems"]:
            system["provider"] = "not recorded"
        run("unknown_providers", record)
        record = copy.deepcopy(base)
        record["claims"][0].pop("produced_by")
        run("contributors_not_reconstructed", record)
        record = copy.deepcopy(base)
        record["claims"][0]["checks"] = []
        run("no_checks", record)
        record = copy.deepcopy(base)
        check = record["claims"][0]["checks"][0]
        check.pop("observed", None)
        check.pop("residual", None)
        run("completed_check_without_result_or_limits", record)
        raw = validator.yaml.safe_dump(base, sort_keys=False)
        needle = "    outcome: passed\n"
        assert needle in raw, "Update the synthetic case if the source record changes."
        raw = raw.replace(needle, "    outcome: failed\n" + needle, 1)
        run("duplicate_outcome", raw=raw.encode("utf-8"))
        for date in ["2026-02-30", "2026-13", "0000", "2026-99-99"]:
            record = copy.deepcopy(base)
            record["record"]["prepared_on"] = date
            run(f"impossible_date_{date}", record)
        run("invalid_utf8", raw=b"\xff\n")


if __name__ == "__main__":
    main()
