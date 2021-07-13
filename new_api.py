from flask import Flask, request
from flask import jsonify

# Let's import our functions:
import tools.get_functions as get
import tools.post_functions as post
import tools.sia_functions as sia_f

app = Flask(__name__)


# GET:

@app.route("/")
def index():
    return "LA API ESTA FUNCIONANDO!"


@app.route("/messages")
def mensajes_todos():
    mensajes = get.obtener_mensajes()
    return jsonify(mensajes)


@app.route("/users")
def usuarios_todos():
    usuarios = get.obtener_usuarios()
    return jsonify(usuarios)


@app.route("/chats")
def chats_todos():
    chats = get.obtener_chats()
    return jsonify(chats)


@app.route("/messages/<chat_id>/<user_id>")
def mensaje(chat_id, user_id):
    mensajes = get.obtener_mensajes_usuario(chat_id, user_id)
    return jsonify(mensajes)


@app.route("/sia/users")
def sia_usuarios():
    sias_promedio = get.obtener_sia_usuarios()
    return jsonify(sias_promedio)


@app.route("/sia/user/<user_id>")
def sia_usuario(user_id):
    sia_promedio = get.obtener_sia_usuario(user_id)
    return jsonify(sia_promedio)


@app.route("/sia/chats")
def sia_chats():
    sias_promedio = get.obtener_sia_chats()
    return jsonify(sias_promedio)


@app.route("/sia/chat/<chat_id>")
def sia_chat(chat_id):
    sia_promedio = get.obtener_sia_chat(chat_id)
    return jsonify(sia_promedio)





# POST:

@app.route("/create_chat/<chat_name>", methods=["POST", "GET"])
def insertar_grupo(chat_name):
    post.crear_grupo(chat_name)
    return "Se ha creado el grupo!"


@app.route("/create_user", methods=["POST"])
def insertar_usuario():
    slack_id = request.form.get("slack_id")
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    post.crear_usuario(slack_id, first_name, last_name)
    return "Se ha creado el usuario!"


@app.route("/create_message", methods=["POST"])
def insertar_mensaje():
    chat_id = request.form.get("chat_id")
    user_id = request.form.get("user_id")
    content = request.form.get("content")
    post.crear_mensaje(chat_id, user_id, content)
    return "Se ha creado el mensaje!"


@app.route("/user_to_chat", methods=["POST"])
def unir_usuario_chat():
    chat_id = request.form.get("chat_id")
    user_id = request.form.get("user_id")
    post.union_usuario_chat(chat_id, user_id)
    return "Se ha unido el usuario al chat!"





app.run(debug=True)