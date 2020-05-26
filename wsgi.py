from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "THIS IS AN HELLO WORLD FOR BE"

if __name__ == "__main__":
    application.run()
