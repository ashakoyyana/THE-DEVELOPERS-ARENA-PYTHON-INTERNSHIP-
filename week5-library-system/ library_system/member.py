from datetime import datetime

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.joined_date = datetime.now().strftime('%Y-%m-%d')
        self.borrowed_books = []

    def borrow_book(self, isbn):
        self.borrowed_books.append(isbn)

    def return_book(self, isbn):
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "joined_date": self.joined_date,
            "borrowed_books": self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data):
        member = cls(data["member_id"], data["name"])
        member.joined_date = data["joined_date"]
        member.borrowed_books = data["borrowed_books"]
        return member

    def __str__(self):
        return f"{self.member_id} - {self.name}"
