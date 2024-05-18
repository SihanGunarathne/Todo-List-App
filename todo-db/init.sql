CREATE DATABASE todo_db;
USE todo_db;


CREATE TABLE todo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(200),
    completed BOOLEAN DEFAULT FALSE
);