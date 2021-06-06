from flask import Flask, render_template, redirect, request
from flask import Blueprint

from models.book import Book

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

books_blueprint = Blueprint("books",__name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", books = books)


@books_blueprint.route("/books/new")
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", authors = authors)

# CREATE
# POST
@books_blueprint.route("/books", methods=['POST'])
def create_book():
    # date from form
    title = request.form['title']
    author_id = request.form['author_id']
    genre = request.form['genre']
    publisher = request.form['publisher']
    available = request.form['available']
    # create a book object form the data
    author = author_repository.select(author_id)
    new_book = Book(title, author, genre, publisher, available)
    # save the object to db
    book_repository.save(new_book)
    # redirect to /books
    return redirect("/books")

# EDIT
# GET '/books/<id>/edit'
@books_blueprint.route("/books/<id>/edit")
def edit_book(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template("books/edit.html", book=book, authors=authors)

# UPDATE
# POST 
@books_blueprint.route("/books/<id>", methods=["POST"])
def update_book(id):
    # date from form
    title = request.form['title']
    author_id = request.form['author_id']
    genre = request.form['genre']
    publisher = request.form['publisher']
    available = request.form['available']
    # create a book object form the data
    author = author_repository.select(author_id)
    new_book = Book(title, author, genre, publisher, available)
    book_repository.update(update_book)
    return redirect("/books")


# SHOW
@books_blueprint.route("/books/<id>")
def show_book(id):
    book = book_repository.select(id)
    return render_template("books/show.html", book = book)

# DELETE
# POST
@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")

