from finance_tracker.file_handler import save_expenses, load_expenses

def test_save_and_load():
    data = [{"amount": 50, "category": "Test", "description": "Demo", "date": "2025-01-01"}]
    save_expenses(data)
    loaded = load_expenses()
    assert loaded == data
