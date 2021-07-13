USE slack;

INSERT INTO users (slack_id, first_name, last_name) VALUES
(1, "Cristian", "Castro Blua"),
(2, "Borja", "Cañada"),
(3, "Alvaro", "Garcia"),
(4, "Olaya", "Marques"),
(5, "Santi", "Moreno"),
(6, "Victoria", "Ruiz");


INSERT INTO chats (chat_name) VALUES
("Los locatis"),
("La banda de boedo"),
("Ironhackers");

INSERT INTO connections (user_id, chat_id) VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 2),
(6, 2),
(1, 3),
(2, 3),
(3, 3),
(4, 3),
(5, 3),
(6, 3);

INSERT INTO messages (content, user_id, chat_id) VALUES
("Hola gente!", 1, 1),
("Holas", 2, 1),
("Como estan?", 1, 1),
("Super contento", 2, 1),
("Estoy triste", 5, 2),
("Porque?", 6, 2),
("Vamos a disfrutar!", 1, 3),
("Si!", 3, 3);