from finance_tracker.expense import Expense

def test_expense_creation():
    e = Expense(100, "Food", "Lunch")
    assert e.amount == 100
    assert e.category == "Food"
