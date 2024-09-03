from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    # Импорты и регистрация Blueprints
    from app.routers.questions import bp as question_bp
    from app.routers.response import bp as response_bp
    from app.routers.categories import bp as category_bp

    app.register_blueprint(question_bp)
    app.register_blueprint(response_bp)
    app.register_blueprint(category_bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/questions')
    def questions():
        return render_template('questions.html')

    @app.route('/categories')
    def categories():
        return render_template('categories.html')

    return app
