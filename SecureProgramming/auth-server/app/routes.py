import uuid
from flask import Blueprint, request, jsonify, render_template, redirect
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from .helpers import validate_password, hash_password, check_password, generate_random_string
from .database import db, User
from .cache import redis_client

routes_bp = Blueprint('routes', __name__, template_folder='templates')


@routes_bp.route("/register", methods=["GET"])
def register():
    return render_template('register.html')


@routes_bp.route("/create-user", methods=["POST"])
def create_user():
    username = request.form.get("username")
    password = request.form.get("password")

    user_registered = db.session.execute(db.select(User).filter_by(username=username)).scalar_one_or_none()
    if user_registered:
        return jsonify({"msg": "User already exists"}), 400

    valid, message = validate_password(password)
    if not valid:
        return jsonify({"msg": message}), 400

    hashed_password = hash_password(password)
    user = User(
        username=username,
        password=hashed_password,
    )
    db.session.add(user)
    db.session.commit()
    print(user)
    return jsonify({"msg": "User registered successfully"}), 201


@routes_bp.route("/login", methods=["GET"])
def login():
    return render_template('login.html', redirect_url="https://cct-app.ie")


@routes_bp.route("/credentials", methods=["POST"])
def credentials():
    username = request.form.get("username")
    password = request.form.get("password")
    redirect_url = request.args.get("redirect_url")

    user = db.session.execute(db.select(User).filter_by(username=username)).scalar_one_or_none()
    if not user:
        return jsonify({"msg": "Invalid username or password"}), 401

    hashed_password = user.password
    if not hashed_password or not check_password(password, hashed_password):
        return jsonify({"msg": "Invalid username or password"}), 401


    short_lived_token = str(uuid.uuid4())
    redis_client.setex(f"token:{short_lived_token}", 600, user.username)  # 600 seconds = 10 minutes
    redirect_url += "?short_lived_token=" + short_lived_token
    return redirect(redirect_url)


@routes_bp.get("/access_token")
def get_access_token():
    short_lived_token = request.args.get("short_lived_token", "")
    username = redis_client.get(f"token:{short_lived_token}")
    if not username:
        return jsonify({"msg": "Invalid Token!"}), 401

    access_token = create_access_token(identity=username)
    return jsonify({"access_token": access_token}), 200


@routes_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"msg": f"Hello, {current_user}. This is a protected route!"}), 200

