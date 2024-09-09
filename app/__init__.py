from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/emirz/Desktop/Apps/Python/TaskApp/task.db'

    db.init_app(app)

    # Blueprint (routes) import
    from .routes import task_blueprint
    app.register_blueprint(task_blueprint)

    return app
