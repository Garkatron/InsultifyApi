from flask import Flask, jsonify, request
import json
import random

app = Flask(__name__)

insults = {}

try:
    with open("insult.json", "r") as file:
        insults = json.load(file)
except FileNotFoundError:
    print("The file insult.json not found.")
    insults = {}
except json.JSONDecodeError:
    print("Error on decode JSON.")
    insults = {}


@app.route("/insult/<lang>", methods=["GET"])
def get_insult(lang):

    if lang in insults:
        return jsonify({"insult": random.choice(insults[lang])}), 200
    else:
        return jsonify({"error": "Lang no supported."}), 400  # 400 = Bad Request

if __name__=="__main__":
    app.run(debug=True)

# End point

"""@app.route("/users/<user_id>")
def get_user(user_id):
    user = {
        "id": user_id, "name": "test", "tfno": "000"
    }

    # /users/23e23?query=query_test

    query = request.args.get("query")
    if query:
        user["query"] = query


    return jsonify(user), 200 # 200 = todo bien"""

# End point para obtener un insulto en el idioma especificado

"""
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    data["status"]="user created"
    return jsonify(data), 201 # 201 info creada
"""

# Get->Obtener
# Put->Actualizar
# Post->Crear