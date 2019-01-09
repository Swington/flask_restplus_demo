from flask import Flask
from flask_restplus import Api

from config import load_config_by_name, get_config
from controllers import hello_ns
from models import db


def create_app(config_name):
    config = load_config_by_name(config_name)
    app = Flask(config['server']['NAME'])
    app.config.update(config['server'])

    api = Api(app, doc='/doc/')
    api.add_namespace(hello_ns, path='/hello')

    db.init_app(app)

    return app


if __name__ == '__main__':
    app = create_app('prod')
    app.run(debug=True, port=get_config()['server']['PORT'])
