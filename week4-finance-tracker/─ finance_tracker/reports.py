from collections import defaultdict

def category_breakdown(expenses):
    """
    Returns total amount spent per category
    """
    summary = defaultdict(float)

    for expense in expenses:
        summary[expense["category"]] += expense["amount"]

    return dict(summary)
