#!/usr/bin/env python3

import os

from flask import Flask
from flask_cors import CORS

from transport.flask import TasksTransport

app_name = __name__

# For locals tests
os.environ['TZ'] = 'GMT'
basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    """
        App creation function
    """
    a = Flask(app_name)
    database = os.path.join(basedir, 'test.db')
    if not os.path.exists(database):
        raise ValueError('Invalid database path: {}'.format(database))

    print(database)
    a.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database
    a.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(a, supports_credentials=True)

    TasksTransport.register(a)
    # from your_talent.oauth import config_oauth
    # config_oauth(a)
    return a


app = create_app()

if __name__ == '__main__':
    app.run()
