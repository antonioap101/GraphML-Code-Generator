// Database Connection Code
import { Sequelize } from 'sequelize';

const sequelize = new Sequelize('default', 'postgres', '1234', {
    host: 'localhost',
    port: 5432,
    dialect: 'postgres', // Cambia a 'mysql' o 'sqlite' según el DBMS
    logging: false, // Opcional: desactiva el logging de Sequelize
});

export async function ensureTableExists(): Promise<void> {
    const createTableQuery = `
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(250),
            email VARCHAR(250) UNIQUE,
            age INTEGER
        );
    `;
    try {
        await sequelize.query(createTableQuery); // Ejecuta el query raw para crear la tabla
    } catch (error) {
        console.error('Error ensuring table exists:', error);
        throw error;
    }
}

export class UsersDao {
    static async insert(name: string, email: string, age: number): Promise<any> {
        if (name.length < 3) {
            throw new Error("name must be at least 3 characters long");
        }
        if (name.length > 50) {
            throw new Error("name must be less than 50 characters");
        }
        const query = `
            INSERT INTO users (name, email, age)
            VALUES ($1, $2, $3)
            RETURNING *;
        `;
        const values = [name, email, age];
        try {
            const [result] = await sequelize.query(query, { bind: values });
            return result[0]; // Devuelve el primer registro
        } catch (error) {
            console.error('Error inserting record:', error);
            throw error;
        }
    }

    static async selectById(id: number): Promise<any> {
        const query = `
            SELECT * FROM users
            WHERE id = $1;
        `;
        try {
            const [result] = await sequelize.query(query, { bind: [id] });
            return result[0]; // Devuelve el primer registro
        } catch (error) {
            console.error('Error selecting record:', error);
            throw error;
        }
    }

    static async updateById(id: number, name: string, email: string, age: number): Promise<any> {
        if (name.length < 3) {
            throw new Error("name must be at least 3 characters long");
        }
        if (name.length > 50) {
            throw new Error("name must be less than 50 characters");
        }
        const query = `
            UPDATE users
            SET name = $1, email = $2, age = $3
            WHERE id = $4
            RETURNING *;
        `;
        const values = [name, email, age, id];
        try {
            const [result] = await sequelize.query(query, { bind: values });
            return result[0]; // Devuelve el primer registro actualizado
        } catch (error) {
            console.error('Error updating record:', error);
            throw error;
        }
    }

    static async deleteById(id: number): Promise<void> {
        const query = `
            DELETE FROM users
            WHERE id = $1;
        `;
        try {
            await sequelize.query(query, { bind: [id] });
        } catch (error) {
            console.error('Error deleting record:', error);
            throw error;
        }
    }
}

