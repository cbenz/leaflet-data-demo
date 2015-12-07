from flask import Flask, jsonify, request


app = Flask(__name__)
app.debug = True


@app.route("/positions.json")
def positions():
    print request.args
    return jsonify({"a": 1})


if __name__ == "__main__":
    app.run()
