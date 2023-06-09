from flask import Flask
from server.objects import clearMine_socketio
from server.routes import clearMine_blueprint
from flask_cors import CORS


def create_app(debug = True):
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'minesweeper'
    app.register_blueprint(clearMine_blueprint)
    clearMine_socketio.init_app(app)
    CORS(app, supports_credentials=True)
    return app


if __name__ == '__main__':
    app = create_app()
    clearMine_socketio.run(app, host='192.168.127.223', port=26666)


