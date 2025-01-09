class UsersDAO:

    def __init__(self, connection):
        self.connection = connection

    def create(self, name: str, email: str, age: int):
        query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s);"
        with self.connection.cursor() as cursor:
            parameters = [name, email, age]
            cursor.execute(query, parameters)
            self.connection.commit()
            return cursor.fetchone()[0]

    def read(self, id):
        query = "SELECT * FROM users WHERE id = %s;"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (id,))
            return cursor.fetchone()

    def update(self, id, name: str, email: str, age: int):
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


