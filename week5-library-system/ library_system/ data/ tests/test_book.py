from library_system.book import Book

def test_book_checkout():
    book = Book("Python", "Author", "123")
    status, _ = book.check_out("MEM001")
    assert status is True
