CREATE DATABASE users;
USE users;
CREATE TABLE persons(
    id int auto_increment primary key not null,
    userName varchar(50),
    lastName varchar(50),
    Gender varchar(50)
);

INSERT INTO users values(null, "Frank", "Gomez", "Masculino");

SELECT * FROM users;