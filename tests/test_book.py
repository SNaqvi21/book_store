from lib.book import Book

"""
Contruct with id, title, author_name
"""
def test_book_constructs():
    book = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert book.id == 1
    assert book.title == 'Nineteen Eighty-Four'
    assert book.author_name == 'George Orwell'

def test_books_are_equal():
    book1 = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    book2 = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert book1 == book2

def test_formatted_nicely():
    book1 = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert str(book1) == "Book(1, Nineteen Eighty-Four, George Orwell)"

