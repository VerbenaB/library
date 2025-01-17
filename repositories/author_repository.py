from db.run_sql import run_sql 
from models.author import Author


def save(author):
    sql = "INSERT INTO authors (first_name, last_name) VALUES(%s, %s) RETURNING * "
    values = [author.first_name, author.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id

def select_all():
    authors = []
    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['first_name'], row['last_name'], row['id'])
        authors.append(author)

    return authors
    
   
def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)

def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)

    if len(result) > 0:
        author_dict = result[0]
        author = Author(author_dict['first_name'], author_dict['last_name'], author_dict['id'])   
    return author   
