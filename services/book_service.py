
# services/book_service.py
from utils.db_connection import get_connection


def add_book(title, author_id, genre_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO books (title, author_id, genre_id) VALUES (%s, %s, %s)",
        (title, author_id, genre_id)
    )
    conn.commit()
    cur.close()
    conn.close()

def find_books_by_title(title):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT b.id, b.title, a.name, g.name FROM books b "
        "JOIN authors a ON b.author_id = a.id "
        "JOIN genres g ON b.genre_id = g.id "
        "WHERE b.title ILIKE %s", (f"%{title}%",)
    )
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
