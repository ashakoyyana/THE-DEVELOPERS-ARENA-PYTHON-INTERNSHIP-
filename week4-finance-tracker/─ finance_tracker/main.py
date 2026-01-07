from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.reports import category_breakdown
from finance_tracker.utils import print_header

class FinanceTracker:
    def __init__(self):
        self.manager = ExpenseManager()

    def run(self):
        print_header("PERSONAL FINANCE TRACKER")

        while True:
            print("\n1. Add New Expense")
            print("2. View All Expenses")
            print("3. Category Breakdown")
            print("0. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.view_categories()
            elif choice == "0":
                print("Thank you for using Finance Tracker!")
                break
            else:
                print("Invalid choice!")

    def add_expense(self):
        amount = input("Amount: ")
        category = input("Category: ")
        description = input("Description: ")
        self.manager.add_expense(amount, category, description)
        print("Expense added successfully!")

    def view_expenses(self):
        print("\n--- ALL EXPENSES ---")
        for e in self.manager.get_all_expenses():
            print(e)

    def view_categories(self):
        print("\n--- CATEGORY BREAKDOWN ---")
        summary = category_breakdown(self.manager.get_all_expenses())
        for k, v in summary.items():
            print(f"{k}: ₹{v}")

def main():
    FinanceTracker().run()
