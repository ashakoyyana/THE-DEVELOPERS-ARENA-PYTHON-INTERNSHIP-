from library_system.library import Library

def test_library_load():
    lib = Library()
    assert lib.books is not None
