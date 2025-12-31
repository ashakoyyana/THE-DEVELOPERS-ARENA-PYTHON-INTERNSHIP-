# Contact Management System
# Week 3 Project - Functions & Dictionaries

import json
import re
from datetime import datetime
import os

DATA_FILE = "contacts_data.json"


def validate_phone(phone):
    digits = re.sub(r'\D', '', phone)
    if 10 <= len(digits) <= 15:
        return True, digits
    return False, None


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_contacts(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


def add_contact(contacts):
    print("\n--- ADD NEW CONTACT ---")

    name = input("Enter contact name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return

    phone = input("Enter phone number: ").strip()
    valid, phone = validate_phone(phone)
    if not valid:
        print("Invalid phone number!")
        return

    email = input("Enter email (optional): ").strip()
    if email and not validate_email(email):
        print("Invalid email format!")
        return

    contacts[name] = {
        "phone": phone,
        "email": email or None,
        "created_at": datetime.now().isoformat()
    }

    save_contacts(contacts)
    print("✅ Contact added successfully!")


def search_contact(contacts):
    term = input("Enter name to search: ").lower()
    found = False

    for name, info in contacts.items():
        if term in name.lower():
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            found = True

    if not found:
        print("No contact found.")


def main():
    contacts = load_contacts()

    while True:
        print("\n--- CONTACT MANAGEMENT SYSTEM ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3.Update contact")
        print("4.delete contact")
        print("5.view contacts")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            print("Goodbye ")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()

