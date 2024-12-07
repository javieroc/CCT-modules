from flask import Flask
from flask_jwt_extended import JWTManager
from .routes import routes_bp
from .database import db

def create_app():
    app = Flask(__name__)
    jwt = JWTManager(app)
    app.config["JWT_SECRET_KEY"] = "your_jwt_secret_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:admin@postgres-db:5432/cctdb"

    db.init_app(app)

    # app.config.from_pyfile('config.py')

    with app.app_context():
        app.register_blueprint(routes_bp)
        db.create_all()

    return app


# if __name__ == "__main__":
#     app = create_app()
#     app.run(host='0.0.0.0', port=3000, debug=True)
