from flask import Flask, jsonify, render_template
from data_to_sql import print_historical_prices, print_current_prices, print_predict_prices, print_buys_simulator
from plot_data import plot_historical_data

app = Flask(__name__)


@app.route('/crypto/', methods=['GET'])
def get_crypto():
    return jsonify(print_current_prices())


@app.route('/crypto/<symbol>/<interval>/', methods=['GET'])
def get_crypto_history(symbol, interval):
    return jsonify(print_historical_prices(symbol, interval))


@app.route('/crypto/<symbol>/<interval>/plot/')
def print_crypto_history(symbol, interval):
    plot_historical_data(symbol,interval)
    return render_template('crypto_history_plot.html',
                           name=f'{symbol}_{interval}',
                           url=f'/static/historical_plot_{symbol}_{interval}.png')


@app.route('/crypto/<symbol>/<interval>/predict/', methods=['GET'])
def get_predict_price(symbol, interval):
    return jsonify(print_predict_prices(symbol, interval))


@app.route('/crypto/<symbol>/<interval>/<float:money>/simulation/', methods=['GET'])
def get_buys_simulation(symbol, interval, money):
    return jsonify(print_buys_simulator(symbol, interval, money))


if __name__ == '__main__':
    app.run(debug=True)
