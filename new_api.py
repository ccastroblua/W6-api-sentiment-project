from flask import Flask, request
from flask import jsonify
import markdown.extensions.fenced_code

# Let's import our functions:
import tools.get_functions as get
import tools.post_functions as post
import tools.sia_functions as sia_f

app = Flask(__name__)


# GET API ENDPOINTS:

@app.route("/")
def index():
    readme_file = open("Readme.md", "r")
    md_template = markdown.markdown(
        readme_file.read(), extensions = ["fenced_code"]
    )
    return md_template

# It provides you all messages information.
@app.route("/messages")
def mensajes_todos():
    mensajes = get.obtener_mensajes()
    return jsonify(mensajes)

#It provides you all users information.
@app.route("/users")
def usuarios_todos():
    usuarios = get.obtener_usuarios()
    return jsonify(usuarios)

# It provides you all chats information.
@app.route("/chats")
def chats_todos():
    chats = get.obtener_chats()
    return jsonify(chats)

# It provides you an specific user messages send in an specific chat.
@app.route("/messages/<chat_id>/<user_id>")
def mensaje(chat_id, user_id):
    mensajes = get.obtener_mensajes_usuario(chat_id, user_id)
    return jsonify(mensajes)

# It provides you each users sentiment analysis base of their messages.
@app.route("/sia/users")
def sia_usuarios():
    sias_promedio = get.obtener_sia_usuarios()
    return jsonify(sias_promedio)

# It provides you an specific users sentiment analysis base of their messages.
@app.route("/sia/user/<user_id>")
def sia_usuario(user_id):
    sia_promedio = get.obtener_sia_usuario(user_id)
    return jsonify(sia_promedio)

# It provides you all chats sentiment analysis base of their messages.
@app.route("/sia/chats")
def sia_chats():
    sias_promedio = get.obtener_sia_chats()
    return jsonify(sias_promedio)

# It provides you an specific chat sentiment analysis base of their messages.
@app.route("/sia/chat/<chat_id>")
def sia_chat(chat_id):
    sia_promedio = get.obtener_sia_chat(chat_id)
    return jsonify(sia_promedio)





# POST API ENDPOINTS:

# It creates a new chat with the name specified.
@app.route("/create_chat/<chat_name>", methods=["POST", "GET"])
def insertar_grupo(chat_name):
    post.crear_grupo(chat_name)
    return "Se ha creado el grupo!"

# It creates in the db a new user where you have to specified it with a dictionary {"slack_id": INT, "first_name": STRING, "last_name": STRING}
@app.route("/create_user", methods=["POST"])
def insertar_usuario():
    slack_id = request.form.get("slack_id")
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    post.crear_usuario(slack_id, first_name, last_name)
    return "Se ha creado el usuario!"

# It creates in the db a new message where you have to specified it with a dictionary {"chat_id": INT, "user_id": INT, "content": STRING}
@app.route("/create_message", methods=["POST"])
def insertar_mensaje():
    chat_id = request.form.get("chat_id")
    user_id = request.form.get("user_id")
    content = request.form.get("content")
    post.crear_mensaje(chat_id, user_id, content)
    return "Se ha creado el mensaje!"

# It joins a user to a chat you have to specified it with a dictionary {"chat_id": INT, "user_id": INT}
@app.route("/user_to_chat", methods=["POST"])
def unir_usuario_chat():
    chat_id = request.form.get("chat_id")
    user_id = request.form.get("user_id")
    post.union_usuario_chat(chat_id, user_id)
    return "Se ha unido el usuario al chat!"





app.run(debug=True)