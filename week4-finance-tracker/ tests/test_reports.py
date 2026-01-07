from finance_tracker.reports import category_breakdown

def test_category_breakdown():
    expenses = [
        {"amount": 100, "category": "Food"},
        {"amount": 50, "category": "Travel"}
    ]
    result = category_breakdown(expenses)
    assert result["Food"] == 100
