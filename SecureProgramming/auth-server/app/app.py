from flask import Flask
from flask_jwt_extended import JWTManager
from .routes import routes_bp
from .database import db

def create_app():
    app = Flask(__name__)
    JWTManager(app)
    app.config.from_pyfile('config.py')

    db.init_app(app)


    with app.app_context():
        app.register_blueprint(routes_bp)
        db.create_all()

    return app


# if __name__ == "__main__":
#     app = create_app()
#     app.run(host='0.0.0.0', port=3000, debug=True)
