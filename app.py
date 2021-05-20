import werkzeug.exceptions
from flask import Flask, jsonify, render_template
from data_to_sql import print_historical_prices, print_current_prices, print_predict_prices, print_buys_simulator
from plot_data import print_linear
from binance_api import download_historical_prices

app = Flask(__name__)


@app.route('/crypto/', methods=['GET'])
def get_crypto():
    """Get all crypto pairs from Binance API

    :return: data in json format
    """
    return jsonify(print_current_prices())


@app.errorhandler(werkzeug.exceptions.BadRequest)
@app.route('/crypto/<symbol>/<interval>/', methods=['GET'])
def get_crypto_history(symbol, interval):
    """Get selected crypto pair historical data from Binance API

    :param str symbol: crypto pair (e.g. BTCUSDT)
    :param str interval: time interval (e.g 1d, 1h, 1m.. more in README file)
    :return: data in json format
    """
    if download_historical_prices(symbol, interval) is not None:
        return jsonify(print_historical_prices(symbol, interval))
    return 'Wrong crypto pair or time interval', 400


@app.errorhandler(werkzeug.exceptions.BadRequest)
@app.route('/crypto/<symbol>/<interval>/plot/')
def print_crypto_history2(symbol, interval):
    """Get line chart selected crypto and time interval from Binance API

    :param str symbol: crypto pair (e.g. BTCUSDT)
    :param str interval: time interval (e.g 1d, 1h, 1m.. more in README file)
    :return: html file with line chart created by plotly library
    """
    if download_historical_prices(symbol, interval) is not None:
        print_linear(symbol, interval)
        return render_template(f'{symbol}_{interval}.html')
    return 'Wrong crypto pair or time interval', 400


@app.errorhandler(werkzeug.exceptions.BadRequest)
@app.route('/crypto/<symbol>/<interval>/predict/', methods=['GET'])
def get_predict_price(symbol, interval):
    """Create linear regression model, predict next day price and get results

    :param str symbol: crypto pair (e.g. BTCUSDT)
    :param str interval: time interval (e.g 1d, 1h, 1m.. more in README file)
    :return: current crypto prices with predicted price for next day and "Buy" or "Stay" suggestion as json
    """
    if download_historical_prices(symbol, interval) is not None:
        return jsonify(print_predict_prices(symbol, interval))
    return 'Wrong crypto pair or time interval', 400


@app.errorhandler(werkzeug.exceptions.BadRequest)
@app.route('/crypto/<symbol>/<interval>/<float:money>/simulate/', methods=['GET'])
def get_buys_simulation(symbol, interval, money):
    """Simulate buying depend on "Buy" or "Stay" suggestions from our model for 1000 records

    :param str symbol: crypto pair (e.g. BTCUSDT)
    :param str interval: time interval (e.g 1d, 1h, 1m.. more in README file)
    :param float money: crypto pair price spend on every purchase
    :return: Simulation result as json (result description in README file)
    """
    if download_historical_prices(symbol, interval) is None:
        return 'Wrong crypto pair or time interval', 400
    elif not isinstance(money, float):
        return 'money is not float type (e.g. 100.0)', 400
    return jsonify(print_buys_simulator(symbol, interval, money))


if __name__ == '__main__':
    app.run(debug=True)
