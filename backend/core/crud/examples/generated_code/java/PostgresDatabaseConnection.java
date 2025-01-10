// Database Connection Code
package com.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class PostgresDatabaseConnection {
    private String URL = "jdbc:postgresql://localhost:5432/default";
    private String USER = "postgres";
    private String PASSWORD = "1234";
    // Default constructor
    public PostgresDatabaseConnection() {
    }

    // Constructor with parameters
    public PostgresDatabaseConnection(String URL, String USER, String PASSWORD) {
        this.URL = URL;
        this.USER = USER;
        this.PASSWORD = PASSWORD;
    }

    public Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }

    public void ensureTableExists() {
        String createTableQuery = "CREATE TABLE Users (id SERIAL NOT NULL PRIMARY KEY UNIQUE, username VARCHAR(250));";
        try (Connection connection = getConnection();
             Statement statement = connection.createStatement()) {
            statement.execute(createTableQuery);
        } catch (SQLException e) {
            e.printStackTrace();
            throw new RuntimeException("Error ensuring table exists", e);
        }
    }
}

