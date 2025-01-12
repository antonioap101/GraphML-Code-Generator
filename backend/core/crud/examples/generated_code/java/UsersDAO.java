
// DAO Code
package com.example;

import java.sql.*;

public class UsersDAO {
    private Connection connection;
    public UsersDAO(Connection connection) {
        this.connection = connection;
    }

    // Create
    public void create(String username) throws SQLException {
        if (username.length() < 2) {
            throw new IllegalArgumentException("username must be at least 2 characters long");
        }
        String sql = "INSERT INTO Users (username) VALUES (%s);";
        try (PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setString(2, username);
            statement.executeUpdate();
        }
    }

    // Read
    public ResultSet read(int id) throws SQLException {
        String sql = "SELECT * FROM Users WHERE id = %s;";
        PreparedStatement statement = connection.prepareStatement(sql);
        statement.setInt(1, id);
        return statement.executeQuery();
    }

    // Update
    public void update(int id, String username) throws SQLException {
        if (username.length() < 2) {
            throw new IllegalArgumentException("username must be at least 2 characters long");
        }
        String sql = "UPDATE Users SET username = %s WHERE id = %s;";
        try (PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setString(2, username);
            statement.setInt(statement.getParameterMetaData().getParameterCount(), id);
            statement.executeUpdate();
        }
    }

    // Delete
    public void delete(int id) throws SQLException {
        String sql = "DELETE FROM Users WHERE id = %s;";
        try (PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setInt(1, id);
            statement.executeUpdate();
        }
    }
}