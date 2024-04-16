from flask import Flask, jsonify
import json
from services.financeNewsService import scrapDataFinanceNews
from environs import Env

app = Flask(__name__)
env = Env()
env.read_env()

@app.route("/")
def index():
    return jsonify({'welcome. Version': env.str("version")})

@app.route("/getDataFinanceNews", methods=["GET"])
def getData():
    data = scrapDataFinanceNews()
    return {'data': json.dumps(data)}    


if __name__ == "__main__":
    app.run(debug=True)
