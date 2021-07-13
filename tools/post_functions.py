from config.configuration import engine

def crear_grupo(chat_name):
    engine.execute(
        f"""
        INSERT INTO chats (chat_name) VALUES
        ('{chat_name}');
        """
    )


def crear_usuario(slack_id, first_name, last_name):
    engine.execute(
        f"""
        INSERT INTO users (slack_id, first_name, last_name) VALUES
        ({slack_id}, '{first_name}', '{last_name}');
        """
    )



def crear_mensaje(chat_id, user_id, content):
    engine.execute(
        f"""
        INSERT INTO messages (chat_id, user_id, content) VALUES
        ({chat_id}, {user_id}, '{content}');
        """
    )   


def union_usuario_chat(chat_id, user_id):
    engine.execute(
        f"""
        INSERT INTO connections (chat_id, user_id) VALUES
        ({chat_id}, {user_id});
        """
    )