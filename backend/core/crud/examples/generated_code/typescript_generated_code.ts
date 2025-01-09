// Database Connection Code
import { Pool, PoolClient } from 'pg';

const pool = new Pool({
  host: 'localhost',
  port: 3000,
  database: 'default',
  user: 'username',
  password: 'password',
});

export async function getConnection(): Promise<PoolClient> {
  return await pool.connect();
}

export async function ensureTableExists(): Promise<void> {
  const createTableQuery = `CREATE TABLE table (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE
);`;
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

import { getConnection } from './connection';
import { PoolClient } from 'pg';

export class TableDao {
  static async insert(table: any): Promise<void> {
    const client: PoolClient = await getConnection();
    const query = `INSERT INTO table () VALUES ();`;
    const values = [];
    try {
      await client.query(query, values);
    } catch (error) {
      console.error('Error inserting record:', error);
      throw error;
    } finally {
      client.release();
    }
  }

  static async selectById(id: number): Promise<any> {
    const client: PoolClient = await getConnection();
    const query = `SELECT * FROM table WHERE id = %s;`;
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

  static async updateById(id: number, table: any): Promise<void> {
    const client: PoolClient = await getConnection();
    const query = `UPDATE table SET  WHERE id = %s;`;
    const values = [, id];
    try {
      await client.query(query, values);
    } catch (error) {
      console.error('Error updating record:', error);
      throw error;
    } finally {
      client.release();
    }
  }

  static async deleteById(id: number): Promise<void> {
    const client: PoolClient = await getConnection();
    const query = `DELETE FROM table WHERE id = %s;`;
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