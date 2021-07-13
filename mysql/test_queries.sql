USE slack;

SELECT *
FROM users;

SELECT *
FROM chats;

SELECT *
FROM connections;

SELECT *
FROM messages
INNER JOIN users
ON messages.user_id = users.user_id
ORDER BY messages.user_id ASC;

SELECT *
FROM messages;

SELECT mess_id, content, messages.user_id, messages.chat_id 
FROM messages
WHERE user_id = 1 AND chat_id = 1;

SELECT *
FROM chats;

DELETE FROM chats
WHERE chat_id = 4;

INSERT INTO chats (chat_id, chat_name) VALUES
(4, "El testeo");

INSERT INTO chats (chat_name) VALUES
('El testeo');

INSERT INTO connections (chat_id, user_id) VALUES
(2, 7);

DELETE FROM connections
WHERE chat_id = 2 AND user_id = 7;

SELECT mess_id, content, emotional_value
FROM messages
WHERE emotional_value IS NULL;

INSERT INTO messages (content, user_id, chat_id) VALUES
('Considero que sos una excelente persona y trabajas muy bien.', 5, 2);

UPDATE messages
SET content = 'La mejor manera de probar el proyecto es así.'
WHERE mess_id = 8;

SELECT Avg(emotional_value) AS average_emotional_value
FROM messages
WHERE user_id = 1;

SELECT user_id, Avg(emotional_value) AS average_emotional_value
FROM messages
GROUP BY user_id;