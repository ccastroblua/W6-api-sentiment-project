from config.configuration import engine
import pandas as pd

def obtener_mensajes():
    
    query = """
    SELECT mess_id, content, messages.user_id, chat_id, first_name, last_name
    FROM messages
    INNER JOIN users
    ON messages.user_id = users.user_id
    ORDER BY messages.user_id ASC;   
    """
    
    data = pd.read_sql_query(query, engine)

    return data.to_json()


def obtener_usuarios():
    
    query = """
    SELECT user_id, first_name, last_name
    FROM users;
    """
    
    data = pd.read_sql_query(query, engine)
    return data.to_json()


def obtener_chats():
    
    query = """
    SELECT chat_id, chat_name, chat_desc
    FROM chats;
    """
    
    data = pd.read_sql_query(query, engine)
    return data.to_json()


def obtener_mensajes_usuario(chat_id, user_id):
    
    query = f"""
    SELECT mess_id, content, messages.user_id, messages.chat_id 
    FROM messages
    WHERE user_id = {user_id} AND chat_id = {chat_id};
    """
    
    data = pd.read_sql_query(query, engine)
    return data.to_json()


def obtener_sia_usuario(user_id):
    query = f"""
    SELECT Avg(emotional_value) AS average_emotional_value
    FROM messages
    WHERE user_id = {user_id};
    """
    
    data = pd.read_sql_query(query, engine)
    return data.to_json()


def obtener_sia_usuarios():
    query = f"""
    SELECT user_id, Avg(emotional_value) AS average_emotional_value
    FROM messages
    GROUP BY user_id;
    """
    
    data = pd.read_sql_query(query, engine)
    return data.to_json()


def obtener_sia_chat(chat_id):
    query = f"""
    SELECT Avg(emotional_value) AS average_emotional_value
    FROM messages
    WHERE chat_id = {chat_id};
    """
    
    data = pd.read_sql_query(query, engine)
    return data.to_json()


def obtener_sia_chats():
    query = f"""
    SELECT chat_id, Avg(emotional_value) AS average_emotional_value
    FROM messages
    GROUP BY chat_id;
    """
    
    data = pd.read_sql_query(query, engine)
    return data.to_json()