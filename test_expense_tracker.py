import json
from pathlib import Path

def test_expense_data_format():
    expense = {
        "date": "2026-10-02",
        "category": "Food",
        "amount": 50000,
        "note": "Lunch"
    }

    assert isinstance(expense["date"], str)
    assert isinstance(expense["category"], str)
    assert isinstance(expense["amount"], (int, float))
    assert isinstance(expense["note"], str)


def test_json_storage(tmp_path):
    data_file = tmp_path / "expenses.json"

    expenses = [
        {
            "date": "2026-10-02",
            "category": "Food",
            "amount": 50000,
            "note": "Lunch"
        }
    ]

    data_file.write_text(
        json.dumps(expenses),
        encoding="utf-8"
    )

    loaded = json.loads(
        data_file.read_text(encoding="utf-8")
    )

    assert loaded == expenses
