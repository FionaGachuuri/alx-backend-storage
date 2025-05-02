-- script thst creates a table users with unique id, email and name
-- CREATE DATABASE IF NOT EXISTS hbtn_0d_tvshows;
-- USE hbtn_0d_tvshows;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);
