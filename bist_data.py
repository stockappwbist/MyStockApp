from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def r_hello_world():
    return jsonify({'msg': 'e'})


if __name__ == '__main__':
    app.run()


