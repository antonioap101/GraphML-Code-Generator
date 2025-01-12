# Database Connection Code
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Database configuration
DB_CONFIG = {
    'dialect': 'postgresql',
    'driver': 'psycopg2',
    'host': 'localhost',
    'port': 5432,
    'database': 'default',
    'username': 'postgres',
    'password': '1234'
}

# Create the connection string
DATABASE_URL = (
    "{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}".format(**DB_CONFIG)
    if DB_CONFIG['dialect'] != "sqlite"
    else "sqlite:///{database}".format(**DB_CONFIG)
)

# Configure the engine and session
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)

@contextmanager
def get_connection():
    """
    Creates a SQLAlchemy session to interact with the database.
    """
    session = Session()
    try:
        yield session
    finally:
        session.close()

def ensure_table_exists():
    """
    Ensures that a table exists in the database.
    """
    create_table_query = """CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(250), email VARCHAR(250) UNIQUE, age INTEGER);"""
    with get_connection() as conn:
        conn.execute(text(create_table_query))
        conn.commit()


# DAO Code
from sqlalchemy import text

class UsersDAO:
    def __init__(self, session):
        # Initialize the DAO with a SQLAlchemy session
        self.session = session

    def create(self, name: str, email: str, age: int):
        if len(name) < 3:
            raise ValueError(f"name must be at least 3 characters long")
        if len(name) > 50:
            raise ValueError(f"name must be less than 50 characters")
        query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s);"
        parameters = (name, email, age)

        # Keep the connection open during the operation
        conn = self.session.connection()
        cursor = conn.connection.cursor()
        cursor.execute(query, parameters)
        conn.connection.commit()
        return cursor.lastrowid

    def read(self, id: int):
        query = "SELECT * FROM users WHERE id = %s;"
        parameters = (id,)

        conn = self.session.connection()
        cursor = conn.connection.cursor()
        cursor.execute(query, parameters)
        return cursor.fetchone()

    def update(self, id: int, name: str, email: str, age: int):
        if len(name) < 3:
            raise ValueError(f"name must be at least 3 characters long")
        if len(name) > 50:
            raise ValueError(f"name must be less than 50 characters")
        query = "UPDATE users SET name = %s, email = %s, age = %s WHERE id = %s;"
        parameters = (name, email, age, id)

        conn = self.session.connection()
        cursor = conn.connection.cursor()
        cursor.execute(query, parameters)
        conn.connection.commit()

    def delete(self, id: int):
        query = "DELETE FROM users WHERE id = %s;"
        parameters = (id,)

        conn = self.session.connection()
        cursor = conn.connection.cursor()
        cursor.execute(query, parameters)
        conn.connection.commit()

