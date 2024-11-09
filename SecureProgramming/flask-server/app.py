from flask import Flask
from flask import make_response
from flask import request
from flask import abort, jsonify
import jwt
import datetime


app = Flask(__name__)


@app.before_request
def test():
    if request.path.startswith("/login"):
        return
    auth_header = request.headers.get("Authorization")
    if auth_header == None:
        abort(make_response(jsonify({"message": "Auth required"}), 401))
    token = auth_header.split(" ")[1]
    token_decoded = {}
    try:
        token_decoded = jwt.decode(token, key="secret", algorithms=["HS256"])
    except:
        return make_response(jsonify({"message": "Auth required"}), 401)
    print(token_decoded)


@app.route("/hello-class")
def hello_class():
    response = make_response("Hello class")
    return response


@app.route("/hello-cct")
def hello_cct():
    return 'Hello CCT'


@app.route("/hello/<name>")
def hello_name(name: str):
    param1 = request.args.get("param2")
    return f"Hello {name} - {param1}"

users = [
    {"name": "david", "password": "test"}
]

@app.route("/register", methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    password = data.get('password')
    users.append({ name, password })
    return jsonify({
        "message": "User registered successfully"
    }), 201


@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    for user in users:
        if user["name"] == username and user["password"] == password:
            return make_response(jsonify({"iss": "https://cct.ie", "token": jwt.encode({"username": username, "exp": (datetime.datetime.now() + datetime.timedelta(minutes=60)).timestamp()}, "secret", algorithm="HS256")}), 200)
    return make_response({"message": "Invalid user"}, 401)


if __name__ == "__main__":
    app.run(debug=True)
