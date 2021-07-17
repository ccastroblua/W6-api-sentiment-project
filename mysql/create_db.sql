DROP DATABASE IF EXISTS slack;
CREATE DATABASE slack;

USE slack;

CREATE TABLE users (
user_id INT PRIMARY KEY AUTO_INCREMENT,
slack_id INT NOT NULL,
first_name VARCHAR(40) NOT NULL,
last_name VARCHAR(40) NOT NULL,
email VARCHAR(40),
phone VARCHAR(20)
);

CREATE TABLE chats (
chat_id INT PRIMARY KEY AUTO_INCREMENT,
chat_name VARCHAR(40) NOT NULL,
chat_desc VARCHAR(100)
);

CREATE TABLE connections (
user_id INT,
chat_id INT,
PRIMARY KEY(user_id, chat_id),
FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE,
FOREIGN KEY(chat_id) REFERENCES chats(chat_id) ON DELETE CASCADE
);

CREATE TABLE messages (
mess_id INT PRIMARY KEY AUTO_INCREMENT,
content VARCHAR(10000),
mess_date DATE, 	# El date debería ser NOT NULL pero para las pruebas iniciales vamos a dejarlo así
emotional_value FLOAT,
user_id INT NOT NULL,
chat_id INT NOT NULL,
FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
FOREIGN KEY (chat_id) REFERENCES chats(chat_id) ON DELETE CASCADE
);


