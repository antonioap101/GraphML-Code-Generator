// Database Connection Code
package com.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class SQLiteDatabaseConnection {
    private String URL = "jdbc:sqlite:default.db";
    private String USER = "username";
    private String PASSWORD = "password";
    // Default constructor
    public SQLiteDatabaseConnection() {
    }

    // Constructor with parameters
    public SQLiteDatabaseConnection(String URL, String USER, String PASSWORD) {
        this.URL = URL;
        this.USER = USER;
        this.PASSWORD = PASSWORD;
    }

    public Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }

    public void ensureTableExists() {
        String createTableQuery = "CREATE TABLE Users (id AUTOINCREMENT NOT NULL PRIMARY KEY UNIQUE, username TEXT);";
        try (Connection connection = getConnection();
             Statement statement = connection.createStatement()) {
            statement.execute(createTableQuery);
        } catch (SQLException e) {
            e.printStackTrace();
            throw new RuntimeException("Error ensuring table exists", e);
        }
    }
}

