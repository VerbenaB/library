from db.run_sql import run_sql 
from models.book import Book
import repositories.author_repository as author_repository 

def save(book):
    sql = "INSERT INTO books (title, author_id, genre, publisher, available) VALUES(%s, %s, %s, %s, %s) RETURNING * "
    values = [book.title, book.author.id, book.genre, book.publisher, book.available]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id

def select_all():
    sql = "SELECT * FROM books"
    results = run_sql(sql)

    books = []
    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], author, row['genre'], row['publisher'], row['available'], row['id'])
        books.append(book)
    return books