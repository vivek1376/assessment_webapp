import os

from flask import Flask


def create_app():
    webapp = Flask(__name__)

    @webapp.route('/')
    def hello():
        return 'Hello, World!'

    return webapp
