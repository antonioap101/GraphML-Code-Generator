from backend.core.crud.examples.generated_code.python.python_mysql_generated_code import get_connection as mysql_get_connection, \
    ensure_table_exists as mysql_ensure_table_exists, UsersDAO as mysql_UsersDAO
from backend.core.crud.examples.generated_code.python.python_postgres_generated_code import get_connection as postgres_get_connection, \
    ensure_table_exists as postgres_ensure_table_exists, UsersDAO as postgres_UsersDAO
from backend.core.crud.examples.generated_code.python.python_sqlite_generated_code import get_connection as sqlite_get_connection, \
    ensure_table_exists as sqlite_ensure_table_exists, UsersDAO as sqlite_UsersDAO

if __name__ == "__main__":
    mysql = mysql_ensure_table_exists, mysql_get_connection, mysql_UsersDAO
    postgres = postgres_ensure_table_exists, postgres_get_connection, postgres_UsersDAO
    sqlite = sqlite_ensure_table_exists, sqlite_get_connection, sqlite_UsersDAO
    mysql_ensure_table_exists()
    with mysql_get_connection() as conn:
        dao = mysql_UsersDAO(conn)
    #
    # postgres_ensure_table_exists()
    # with postgres_get_connection() as conn:
    #     dao = postgres_UsersDAO(conn)

    # sqlite_ensure_table_exists()
    # with sqlite_get_connection() as conn:
    #     dao = sqlite_UsersDAO(conn)

    # Create
    user_id = dao.create("John Doe", "johndoe@email.com", 30)
    # Read
    user = dao.read(user_id)
    print(f"Read user: {user}")
    # Update
    dao.update(user_id, "Jane Doe", "janedoe@email.com", 25)
    # Delete
    dao.delete(user_id)