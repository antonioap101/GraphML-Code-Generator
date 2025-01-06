// Database Connection Code

using System;
using System.Data;
using System.Data.Common;
using System.Data.SqlClient;

public class DatabaseConnection
{
    private const string ConnectionString = "Server=localhost;Database=default;User Id=username;Password=password;";

    public static IDbConnection GetConnection()
    {
        return new SqlConnection(ConnectionString);
    }

    public static void EnsureTableExists()
    {
        string createTableQuery = @"CREATE TABLE table (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE
);";

        using (var connection = GetConnection())
        {
            connection.Open();
            using (var command = connection.CreateCommand())
            {
                command.CommandText = createTableQuery;
                command.ExecuteNonQuery();
            }
        }
    }
}


// DAO Code

using System;
using System.Data;
using System.Data.SqlClient;

public class TableDAO
{
    private readonly SqlConnection _connection;

    public TableDAO(SqlConnection connection)
    {
        _connection = connection;
    }

    // Create
    public void Create()
    {
        string sql = "INSERT INTO table () VALUES ();";
        using (SqlCommand command = new SqlCommand(sql, _connection))
        {

            command.ExecuteNonQuery();
        }
    }

    // Read
    public DataTable Read(int id)
    {
        string sql = "SELECT * FROM table WHERE id = %s;";
        using (SqlCommand command = new SqlCommand(sql, _connection))
        {
            command.Parameters.AddWithValue("@id", id);
            using (SqlDataAdapter adapter = new SqlDataAdapter(command))
            {
                DataTable result = new DataTable();
                adapter.Fill(result);
                return result;
            }
        }
    }

    // Update
    public void Update(int id, )
    {
        string sql = "UPDATE table SET  WHERE id = %s;";
        using (SqlCommand command = new SqlCommand(sql, _connection))
        {

            command.Parameters.AddWithValue("@id", id);
            command.ExecuteNonQuery();
        }
    }

    // Delete
    public void Delete(int id)
    {
        string sql = "DELETE FROM table WHERE id = %s;";
        using (SqlCommand command = new SqlCommand(sql, _connection))
        {
            command.Parameters.AddWithValue("@id", id);
            command.ExecuteNonQuery();
        }
    }
}