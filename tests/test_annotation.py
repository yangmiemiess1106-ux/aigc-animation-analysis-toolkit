from aigc_animation_toolkit.annotation import validate_row


def test_valid_row_has_no_errors():
    row = {field: "value" for field in ("case_id", "title", "source_url", "access_date", "rights_note")}
    assert validate_row(row) == []


def test_required_fields_are_reported():
    assert "missing required field: case_id" in validate_row({})
