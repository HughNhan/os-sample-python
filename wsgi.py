from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello ALL you!"

if __name__ == "__main__":
    application.run()
