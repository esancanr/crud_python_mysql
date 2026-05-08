CREATE DATABASE users;
USE users;
CREATE TABLE persons(
    id int auto_increment primary key not null,
    userName varchar(50) not null,
    lastName varchar(50) not null,
    Gender varchar(50) not null
);

INSERT INTO persons values(null, "Frank", "Gomez", "Masculino");

SELECT * FROM persons;