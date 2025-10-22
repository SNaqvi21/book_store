from lib.book import Book

class BookRepository:
    def __init__(self, connection):
        self._conection = connection
    #  initilises instance with connection

    def all(self):
        rows = self._conection.execute("SELECT * FROM books")
    # exectues the sql query "SELECT * FROM books"
        books = []
        for row in rows:
            book = Book(row['id'], row['title'], row['author_name'])
            books.append(book)
        return books