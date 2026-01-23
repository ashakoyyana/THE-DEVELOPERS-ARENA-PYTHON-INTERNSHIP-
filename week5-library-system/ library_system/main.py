from library_system.library import Library
from library_system.book import Book
from library_system.member import Member

library = Library()

while True:
    print("\n1.Add Book\n2.Add Member\n3.Borrow Book\n4.Return Book\n5.Search Books\n6.View Books\n7.Overdue Books\n9.Save & Exit\n0.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        library.add_book(Book(input("Title: "), input("Author: "), input("ISBN: "), input("Year: ")))
    elif choice == "2":
        library.add_member(Member(input("Member ID: "), input("Name: ")))
    elif choice == "3":
        print(library.borrow_book(input("ISBN: "), input("Member ID: "))[1])
    elif choice == "4":
        print(library.return_book(input("ISBN: "))[1])
    elif choice == "5":
        for b in library.search_books(input("Search keyword: ")):
            print(b)
    elif choice == "6":
        for b in library.books.values():
            print(b)
    elif choice == "7":
        for b in library.overdue_books():
            print(b)
    elif choice == "9":
        library.save_data()
        print("Saved successfully.")
        break
    elif choice == "0":
        break
