from flask import Flask

shaeq = Flask(__name__)

@shaeq.route("/")
def hello():
    return "Hello!"

@shaeq.route("/lol")
def addition():
    return "ahahahahha"

@shaeq.route("/knock")
def test():
    return "who is there?"

if __name__ == '__main__':
    shaeq.run()
