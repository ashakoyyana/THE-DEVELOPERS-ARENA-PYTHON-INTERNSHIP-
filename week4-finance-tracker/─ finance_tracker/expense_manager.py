from finance_tracker.expense import Expense
from finance_tracker.file_handler import load_expenses, save_expenses

class ExpenseManager:
    def __init__(self):
        self.expenses = load_expenses()

    def add_expense(self, amount, category, description):
        expense = Expense(amount, category, description)
        self.expenses.append(expense.to_dict())
        save_expenses(self.expenses)

    def get_all_expenses(self):
        return self.expenses
