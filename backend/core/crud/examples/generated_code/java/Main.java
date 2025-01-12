package com.example;

import java.sql.SQLException;


public class Main {
    public static void main(String[] args) {
        // Database Connection Code
//        var dbConnection = new PostgresDatabaseConnection();
//        var dbConnection = new MySQLDatabaseConnection();
        var dbConnection = new SQLiteDatabaseConnection();
        try {
            dbConnection.ensureTableExists();
            // Create a new TableDAO object
            UsersDAO tableDAO = new UsersDAO(dbConnection.getConnection());
            // Create a new record
//            tableDAO.create("Alice");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}