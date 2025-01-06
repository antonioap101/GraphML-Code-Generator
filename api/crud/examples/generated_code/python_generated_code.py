// Database
Connection
Code

import psycopg2
from psycopg2 import sql
from contextlib import contextmanager

DB_CONFIG = {
    'host': 'localhost',
    'port': 3000,
    'database': 'default',
    'user': 'username',
    'password': 'password'
}


@contextmanager
def get_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    try:
        yield conn
    finally:
        conn.close()


def ensure_table_exists():
    create_table_query = """CREATE TABLE table (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE
);"""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(create_table_query)
            conn.commit()

// DAO
Code


class TableDAO:

    @staticmethod
    def create():
        query = """INSERT INTO table () VALUES () RETURNING id;"""
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, ())
                conn.commit()
                return cursor.fetchone()[0]

    @staticmethod
    def read(id):
        query = """SELECT * FROM table WHERE id = %s;"""
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id,))
                return cursor.fetchone()

    @staticmethod
    def update(id, ):
        query = """UPDATE table SET  WHERE id = %s;"""
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id,))
                conn.commit()

    @staticmethod
    def delete(id):
        query = """DELETE FROM table WHERE id = %s;"""
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id,))
                conn.commit()