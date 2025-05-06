
# services/member_service.py

from utils.db_connection import get_connection

def register_member(name, email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO members (name, email) VALUES (%s, %s)",
        (name, email)
    )
    conn.commit()
    cur.close()
    conn.close()

def get_all_members():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM members")
    members = cur.fetchall()
    cur.close()
    conn.close()
    return members
