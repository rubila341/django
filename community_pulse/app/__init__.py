from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Создание экземпляров SQLAlchemy и Migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Инициализация SQLAlchemy и Migrate
    db.init_app(app)
    migrate.init_app(app, db)

    # Импорт и регистрация маршрутов
    from app.routers.questions import bp as question_bp
    from app.routers.response import bp as response_bp
    app.register_blueprint(question_bp)
    app.register_blueprint(response_bp)

    # Дефолтный маршрут
    @app.route('/')
    def index():
        return 'Hello, World!'

    return app
