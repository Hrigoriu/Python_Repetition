"""main.py

MedAssistant v2 entry point. Orchestration only:

    JSON -> PatientRecord.from_dict() (validation) -> list[PatientRecord]
         -> statistics -> report -> save

Helper modules only RAISE exceptions; this file is the one place that
decides how a problem is shown to the user.
"""

import json
import sys
from pathlib import Path

from patient_record import build_records
from report_utils import build_report, save_report
from statistics_utils import calculate_statistics

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "patients.json"
REPORT_PATH = BASE_DIR / "data" / "report.txt"


def read_json(path: Path) -> object:
    """Read and decode a JSON file."""
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main(data_path: Path = DATA_PATH, report_path: Path = REPORT_PATH) -> int:
    """Run the whole pipeline.

    Returns:
        int: 0 on success, 1 on any handled failure (usable as exit code).
    """
    print("MEDASSISTANT")
    print("============\n")

    try:
        print("Loading JSON...")
        raw_records = read_json(data_path)
        print("✓ JSON loaded\n")

        print("Validating records...")
        records, skipped = build_records(raw_records)
        if skipped:
            print(f"⚠ {len(skipped)} record(s) skipped:")
            for item in skipped:
                print(f"  index {item.index} ({item.label}):")
                for reason in item.reasons:
                    print(f"    - {reason}")
        print(f"✓ {len(records)} valid record(s)\n")

        print("Calculating statistics...")
        stats = calculate_statistics(records)
        print("✓ Statistics calculated\n")

        print("Generating report...")
        save_report(report_path, build_report(stats, skipped))
        print(f"✓ Report saved: {report_path.name}")

    except FileNotFoundError as error:
        print(f"✗ File not found:\n  {error.filename}")
        return 1
    except json.JSONDecodeError as error:  # must come BEFORE ValueError (its parent)
        print(f"✗ Invalid JSON:\n  {error}")
        return 1
    except ValueError as error:
        print(f"✗ {error}")
        return 1
    except OSError as error:
        print(f"✗ File error: {error}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())