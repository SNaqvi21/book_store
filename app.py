from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository

# connecting to the database
connection = DatabaseConnection()
connection.connect()

# seeding with seed data extracted from seeds/book_store.sql
connection.seed("seeds/book_store.sql")

# retrieving all books
book_repository = BookRepository(connection)
books = book_repository.all()

# listing the books in the correct format
for book in books:
    print(book)