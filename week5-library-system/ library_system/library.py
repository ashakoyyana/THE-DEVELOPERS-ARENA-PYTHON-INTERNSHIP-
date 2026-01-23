import json
import os
from .book import Book
from .member import Member

BOOKS_FILE = "data/books.json"
MEMBERS_FILE = "data/members.json"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(BOOKS_FILE):
            with open(BOOKS_FILE, "r") as f:
                for b in json.load(f):
                    book = Book.from_dict(b)
                    self.books[book.isbn] = book

        if os.path.exists(MEMBERS_FILE):
            with open(MEMBERS_FILE, "r") as f:
                for m in json.load(f):
                    member = Member.from_dict(m)
                    self.members[member.member_id] = member

    def save_data(self):
        with open(BOOKS_FILE, "w") as f:
            json.dump([b.to_dict() for b in self.books.values()], f, indent=4)

        with open(MEMBERS_FILE, "w") as f:
            json.dump([m.to_dict() for m in self.members.values()], f, indent=4)

    def add_book(self, book):
        self.books[book.isbn] = book

    def add_member(self, member):
        self.members[member.member_id] = member

    def borrow_book(self, isbn, member_id):
        book = self.books.get(isbn)
        member = self.members.get(member_id)
        if not book or not member:
            return False, "Invalid book or member"
        success, msg = book.check_out(member_id)
        if success:
            member.borrow_book(isbn)
        return success, msg

    def return_book(self, isbn):
        book = self.books.get(isbn)
        if not book:
            return False, "Book not found"
        member = self.members.get(book.borrowed_by)
        if member:
            member.return_book(isbn)
        return book.return_book()

    def search_books(self, keyword):
        return [b for b in self.books.values()
                if keyword.lower() in b.title.lower()
                or keyword.lower() in b.author.lower()
                or keyword == b.isbn]

    def overdue_books(self):
        return [b for b in self.books.values() if b.is_overdue()]
