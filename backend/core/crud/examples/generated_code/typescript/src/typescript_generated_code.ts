// Database Connection Code
import { Pool, PoolClient } from 'pg';

const pool = new Pool({
    host: 'localhost',
    port: 5432,
    database: 'default',
    user: 'postgres',
    password: '1234',
});

export async function getConnection(): Promise<PoolClient> {
    return await pool.connect();
}

export async function ensureTableExists(): Promise<void> {
    const createTableQuery = `CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY SERIAL, name VARCHAR(250), email VARCHAR(250) UNIQUE, age INTEGER);`;
    const client = await getConnection();
    try {
        await client.query(createTableQuery);
    } catch (error) {
        console.error('Error ensuring table exists:', error);
        throw error;
    } finally {
        client.release();
    }
}

// DAO Code
export class UsersDao {
    static async insert(name: string, email: string, age: number): Promise<any> {
        if (name.length < 3) {
            throw new Error("name must be at least 3 characters long");
        }
        if (name.length > 50) {
            throw new Error("name must be less than 50 characters");
        }
        const client: PoolClient = await getConnection();
        const query = `INSERT INTO users (name, email, age) VALUES ($1, $2, $3, $4) RETURNING *;`;
        const values = [name, email, age];
        try {
            const result = await client.query(query, values);
            return result.rows[0];
        } catch (error) {
            console.error('Error inserting record:', error);
            throw error;
        } finally {
            client.release();
        }
    }

    static async selectById(id: number): Promise<any> {
        const client: PoolClient = await getConnection();
        const query = `SELECT * FROM users WHERE id = $1;`;
        try {
            const result = await client.query(query, [id]);
            return result.rows[0];
        } catch (error) {
            console.error('Error selecting record:', error);
            throw error;
        } finally {
            client.release();
        }
    }

    static async updateById(id: number, name: string, email: string, age: number): Promise<any> {
        if (name.length < 3) {
            throw new Error("name must be at least 3 characters long");
        }
        if (name.length > 50) {
            throw new Error("name must be less than 50 characters");
        }
        const client: PoolClient = await getConnection();
        const query = `UPDATE users SET name = $1, email = $2, age = $3 WHERE id = $1 RETURNING *;`;
        const values = [name, email, age, id];
        try {
            const result = await client.query(query, values);
            return result.rows[0];
        } catch (error) {
            console.error('Error updating record:', error);
            throw error;
        } finally {
            client.release();
        }
    }

    static async deleteById(id: number): Promise<void> {
        const client: PoolClient = await getConnection();
        const query = `DELETE FROM users WHERE id = $1;`;
        try {
            await client.query(query, [id]);
        } catch (error) {
            console.error('Error deleting record:', error);
            throw error;
        } finally {
            client.release();
        }
    }
}

