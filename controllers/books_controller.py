from flask import Flask, render_template, redirect, request
from flask import Blueprint

from models.book import Book


import repositories.book_repository as book_repository

books_blueprint = Blueprint("books",__name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)

# @books_blueprint.route("/")

