from flask import Flask, jsonify
from data_to_sql import print_historical_prices, print_current_prices


app = Flask(__name__)


@app.route('/crypto/', methods=['GET'])
def get_crypto():
    return jsonify(print_current_prices())


@app.route('/crypto/<symbol>/<interval>/', methods=['GET'])
def get_crypto_history(symbol, interval):
    return jsonify(print_historical_prices(symbol, interval))


if __name__ == '__main__':
    app.run(debug=True)
