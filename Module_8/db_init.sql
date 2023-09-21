CREATE USER 'root21'@'localhost' IDENTIFIED WITH mysql_native_password BY 'SQLFung29!';
DROP USER IF EXISTS 'root21'@'localhost';
GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';