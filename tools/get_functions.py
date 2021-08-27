from config.configuration import engine
import pandas as pd

def obtener_mensajes():
    """
    Getting messages from MySQL DB table messages joined with each user information (first name, last name and id).
  
    Parameters:
    None
  
    Returns:
    string: Jsonized query with all the information.
  
    """
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
    """
    Getting users with user id, first name and last name from users table in MySQL DB.

    Returns:
    string: Jsonized query with all the information.
    """
    query = """
    SELECT user_id, first_name, last_name
    FROM users;
    """
    
    data = pd.read_sql_query(query, engine)
    return data.to_json()


def obtener_chats():
    """
    Getting chats with chat id, name and description from chats table in MySQL DB.

    Returns:
    string: Jsonized query with all the information.
    """    
    query = """
    SELECT chat_id, chat_name, chat_desc
    FROM chats;
    """
    
    data = pd.read_sql_query(query, engine)
    return data.to_json()


def obtener_mensajes_usuario(chat_id, user_id):
    """
    Getting message from an specific chat and user.

    Parameters:
    chat_id (int): Chat's id
    user_id (int): User's id

    Returns:
    string: Jsonized string with specific message information.
    """    
    query = f"""
    SELECT mess_id, content, messages.user_id, messages.chat_id 
    FROM messages
    WHERE user_id = {user_id} AND chat_id = {chat_id};
    """
    
    data = pd.read_sql_query(query, engine)
    return data.to_json()


def obtener_sia_usuario(user_id):
    """
    Getting polarity value from an specific user.

    Parameters:
    user_id (int): User's id

    Returns:
    string: Jsonized string with user's id polarity value.
    """    
    query = f"""
    SELECT Avg(emotional_value) AS average_emotional_value
    FROM messages
    WHERE user_id = {user_id};
    """
    
    data = pd.read_sql_query(query, engine)
    return data.to_json()


def obtener_sia_usuarios():
    """
    Getting polarity average values from all users.

    Returns:
    string: Jsonized string with user's id and average polarity value.
    """    
    query = f"""
    SELECT user_id, Avg(emotional_value) AS average_emotional_value
    FROM messages
    GROUP BY user_id;
    """
    
    data = pd.read_sql_query(query, engine)
    return data.to_json()


def obtener_sia_chat(chat_id):
    """
    Getting polarty average value of a specific group.

    Parameters:
    chat_id (int): Chat's id.

    Returns:
    string: Jsonized string with average polarity value from a specific chat group.
    """    
    query = f"""
    SELECT Avg(emotional_value) AS average_emotional_value
    FROM messages
    WHERE chat_id = {chat_id};
    """
    
    data = pd.read_sql_query(query, engine)
    return data.to_json()


def obtener_sia_chats():
    """Getting polarity average value from all chats.

    Returns:
        string: Jsonized string with average polarity value from all chat groups. 
    """    
    query = f"""
    SELECT chat_id, Avg(emotional_value) AS average_emotional_value
    FROM messages
    GROUP BY chat_id;
    """
    
    data = pd.read_sql_query(query, engine)
    return data.to_json()