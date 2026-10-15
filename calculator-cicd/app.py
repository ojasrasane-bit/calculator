import os
from flask import Flask, jsonify, render_template, request

from calculator import calculate

app = Flask(__name__)
VERSION = os.environ.get("APP_VERSION", "1.0")


@app.route("/")
def index():
    return render_template("index.html", version=VERSION)


@app.route("/health")
def health():
    return jsonify(status="ok", version=VERSION)


@app.route("/api/calculate", methods=["POST"])
def api_calculate():
    data = request.get_json(silent=True) or {}
    try:
        a = float(data["a"])
        b = float(data["b"])
        result = calculate(a, b, data["op"])
    except (KeyError, TypeError, ValueError) as e:
        return jsonify(error=str(e) or "Invalid input"), 400
    except ZeroDivisionError as e:
        return jsonify(error=str(e)), 400
    return jsonify(result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
