// Database Connection Code
import { Sequelize } from 'sequelize';

const sequelize = new Sequelize('../default.db', 'root', '1234', {
    host: 'localhost',
    port: 5432,
    dialect: 'sqlite',
    logging: false, // Opcional: desactiva el logging de Sequelize
});

export async function ensureTableExists(): Promise<void> {
    const createTableQuery = `
    CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT UNIQUE, age INTEGER);
  `;
    try {
        await sequelize.query(createTableQuery);
    } catch (error) {
        console.error('Error ensuring table exists:', error);
        throw error;
    }
}

export { sequelize };


// DAO Code
export class UsersDao {
    static async insert(name: string, email: string, age: number): Promise<void> {
        if (name.length < 3) {
            throw new Error("name must be at least 3 characters long");
        }
        if (name.length > 50) {
            throw new Error("name must be less than 50 characters");
        }
        const query = `
      INSERT INTO users (name, email, age) VALUES (?, ?, ?);
    `;
        const values = [name, email, age];
        try {
            await sequelize.query(query, { replacements: values });
        } catch (error) {
            console.error('Error inserting record:', error);
            throw error;
        }
    }

    static async selectById(id: number): Promise<any> {
        const query = `
      SELECT * FROM users WHERE id = ?;
    `;
        try {
            const [result] = await sequelize.query(query, { replacements: [id] });
            return result[0];
        } catch (error) {
            console.error('Error selecting record:', error);
            throw error;
        }
    }

    static async updateById(id: number, name: string, email: string, age: number): Promise<void> {
        if (name.length < 3) {
            throw new Error("name must be at least 3 characters long");
        }
        if (name.length > 50) {
            throw new Error("name must be less than 50 characters");
        }
        const query = `
      UPDATE users SET name = ?, email = ?, age = ? WHERE id = ?;
    `;
        const values = [name, email, age, id];
        try {
             await sequelize.query(query, { replacements: values });
        } catch (error) {
            console.error('Error updating record:', error);
            throw error;
        }
    }

    static async deleteById(id: number): Promise<void> {
        const query = `
      DELETE FROM users WHERE id = ?;
    `;
        try {
            await sequelize.query(query, { replacements: [id] });
        } catch (error) {
            console.error('Error deleting record:', error);
            throw error;
        }
    }
}

