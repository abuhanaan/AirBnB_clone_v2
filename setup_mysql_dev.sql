<<<<<<< HEAD
-- Creates the database hbnb_dev_db with already specified parameters
-- Create database with the name hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates a new user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- Sets password for user
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- Grants privileges to user on database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grants select privileges to user on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- Flush privileges
FLUSH PRIVILEGES;
=======
-- Script to create a MySQL server with the database hbnb_dev_db.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
>>>>>>> 08d37e6326007a64b50ce934687b5ed366f577ba
