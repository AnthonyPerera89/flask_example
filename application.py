from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello_world():
    return 'Hello Madhushani, Love you <3 <3'


if __name__ == "__main__":
    application.run(debug=True)