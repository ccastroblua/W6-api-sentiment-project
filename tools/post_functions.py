from config.configuration import engine

def crear_grupo(chat_name):
    """
    Create a group in MySQL DB.
  
    Parameters:
    chat_name (string): Message from a user in the chat.
  
    Returns:
    None
  
    """
    engine.execute(
        f"""
        INSERT INTO chats (chat_name) VALUES
        ('{chat_name}');
        """
    )


def crear_usuario(slack_id, first_name, last_name):
    """
    Create a user in MySQL DB with id, first name and last name.
  
    Parameters:
    slack_id (int): New user id.
    first_name (string): User's first name.
    last_name (string): User's last name.

    Returns:
    None
  
    """
    engine.execute(
        f"""
        INSERT INTO users (slack_id, first_name, last_name) VALUES
        ({slack_id}, '{first_name}', '{last_name}');
        """
    )



def crear_mensaje(chat_id, user_id, content):
    """
    Import a message into MySQL DB from a specific user in a specific chat group.
  
    Parameters:
    chat_id (int): Chat's id where this message will be imported.
    user_id (string): User's id.
    content (string): Message's content.
  
    Returns:
    None
  
    """
    engine.execute(
        f"""
        INSERT INTO messages (chat_id, user_id, content) VALUES
        ({chat_id}, {user_id}, '{content}');
        """
    )   


def union_usuario_chat(chat_id, user_id):
    """
    Create the connection between chat and user in MySQL DB.
  
    Parameters:
    chat_id (int): Chat's id.
    user_id (int): User's id.

    Returns:
    None
  
    """
    engine.execute(
        f"""
        INSERT INTO connections (chat_id, user_id) VALUES
        ({chat_id}, {user_id});
        """
    )