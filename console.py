from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository


author_repository.delete_all()
book_repository.delete_all()


author_1 = Author("Madeleine", "Miller")
author_repository.save(author_1)
author_2 = Author("H.P.", "Lovecraft")
author_repository.save(author_2)

book_1 = Book("The song of Achilles", author_1, "historical fiction", "Bloomsberg")
book_repository.save(book_1)
book_2 = Book("the Whisper in Darkness", author_2, "horror", "Penguin")
book_repository.save(book_2)

# authors = author_repository.select_all()

# test_author = author_repository.select(authors[0].id)

# print(vars(test_author))

# print([ item.__dict__ for item in author_repository.select_all()])

