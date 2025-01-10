# Database Connection Code
from contextlib import contextmanager

import psycopg2

DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'default',
    'user': 'postgres',
    'password': '1234'
}


@contextmanager
def get_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    try:
        yield conn
    finally:
        conn.close()


def ensure_table_exists():
    create_table_query = """CREATE TABLE IF NOT EXISTS users  (id SERIAL PRIMARY KEY, name VARCHAR(250), email VARCHAR(250) UNIQUE, age INTEGER);"""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(create_table_query)
            conn.commit()


# DAO Code
class UsersDAO:
    def __init__(self, connection):
        self.connection = connection

    def create(self, name: str, email: str, age: int):
        if len(name) < 3:
            raise ValueError(f"name must be at least 3 characters long")
        if len(name) > 50:
            raise ValueError(f"name must be less than 50 characters")
        query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s);"
        with self.connection.cursor() as cursor:
            parameters = [name, email, age]
            cursor.execute(query, parameters)
            self.connection.commit()
            return cursor.lastrowid

    def read(self, id):
        query = "SELECT * FROM users WHERE id = %s;"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (id,))
            return cursor.fetchone()

    def update(self, id, name: str, email: str, age: int):
        if len(name) < 3:
            raise ValueError(f"name must be at least 3 characters long")
        if len(name) > 50:
            raise ValueError(f"name must be less than 50 characters")
        query = "UPDATE users SET name = %s, email = %s, age = %s WHERE id = %s;"
        with self.connection.cursor() as cursor:
            parameters = [name, email, age, id]
            cursor.execute(query, parameters)
            self.connection.commit()

    def delete(self, id):
        query = "DELETE FROM users WHERE id = %s;"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (id,))
            self.connection.commit()


if __name__ == "__main__":
    ensure_table_exists()
    with get_connection() as conn:
        dao = UsersDAO(conn)
        user_id = dao.create("John Doe",
                             "johndoe@email.com",
                             30)
