
# services/loan_service.py

from utils.db_connection import get_connection

def loan_book(book_id, member_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO loans (book_id, member_id) VALUES (%s, %s)",
        (book_id, member_id)
    )
    conn.commit()
    cur.close()
    conn.close()

def return_book(loan_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""update loans
                    set return_date = CURRENT_DATE
                    where id = %s""",(loan_id))
    conn.commit()
    cur.close()
    conn.close()


def get_loans_by_member(member_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT l.id, b.title, l.loan_date, l.return_date FROM loans l "
        "JOIN books b ON l.book_id = b.id "
        "WHERE l.member_id = %s ORDER BY l.loan_date DESC",
        (member_id,)
    )
    loans = cur.fetchall()
    cur.close()
    conn.close()
    return loans
