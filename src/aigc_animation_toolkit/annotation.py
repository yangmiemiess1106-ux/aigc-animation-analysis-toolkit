REQUIRED_FIELDS = ("case_id", "title", "source_url", "access_date", "rights_note")


def validate_row(row: dict) -> list[str]:
    """Return actionable errors for one annotation row."""
    errors = []
    for field in REQUIRED_FIELDS:
        if not str(row.get(field, "")).strip():
            errors.append(f"missing required field: {field}")
    return errors
