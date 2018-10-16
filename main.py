from flask import Flask, request, jsonify, redirect
from dictionary import search

app = Flask(__name__, static_url_path='')


@app.route('/', methods=["GET"])
def get():
    return redirect("index.html")


@app.route('/search/<key>', methods=["GET"])
def set(key):
    return jsonify(dict(response=search(key)))


if __name__ == '__main__':
    app.run()
