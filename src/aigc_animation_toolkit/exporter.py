"""Validate and normalize an annotation CSV from the command line."""

import csv
import sys
from pathlib import Path
from typing import Union

from .annotation import REQUIRED_FIELDS, validate_row


def export_csv(source: Union[str, Path], destination: Union[str, Path]) -> int:
    with Path(source).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = [field for field in REQUIRED_FIELDS if field not in (reader.fieldnames or [])]
        if missing:
            raise ValueError("missing columns: " + ", ".join(missing))
        rows = list(reader)
    errors = [f"row {index}: {error}" for index, row in enumerate(rows, 2) for error in validate_row(row)]
    if errors:
        raise ValueError("\n".join(errors))
    fields = reader.fieldnames or list(REQUIRED_FIELDS)
    with Path(destination).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: python -m aigc_animation_toolkit.exporter INPUT.csv OUTPUT.csv")
    try:
        print(f"Exported {export_csv(sys.argv[1], sys.argv[2])} annotation(s).")
    except (OSError, ValueError) as error:
        raise SystemExit(f"error: {error}")
