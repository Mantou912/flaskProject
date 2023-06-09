from flask import Flask
from utils.objects import clearMine_socketio
from utils.routes import clearMine_blueprint
from flask_cors import CORS
from utils import events


def create_app(debug=True):
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'minesweeper'
    app.register_blueprint(clearMine_blueprint)
    clearMine_socketio.init_app(app)
    CORS(app, supports_credentials=True)
    return app


if __name__ == '__main__':
    app = create_app()
    clearMine_socketio.run(app, host='127.0.0.1', port=26666)
