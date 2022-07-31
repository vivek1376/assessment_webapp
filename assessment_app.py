from flask import Flask

# app = Flask(__name__)


# class app:
def create_app():
    print("helloll")
    webapp = Flask(__name__)

    print("!!!create_app")

    @webapp.route('/')
    def hello():
        return 'Hello, World!'

    return webapp
