import psycopg2
from psycopg2 import sql

def get_connection():
    return psycopg2.connect(
        dbname="DU_kniznica",
        user="itstepuser",
        password="itstepuser123!",
        host="localhost",
        port=5432
    )
