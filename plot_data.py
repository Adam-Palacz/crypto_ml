from binance_api import prepare_data
import pandas as pd
import matplotlib.pyplot as plt


def plot_historical_data(symbol, interval):
    df = pd.DataFrame(prepare_data(symbol, interval))
    df = df.drop(['Volume'], axis=1)
    df.plot()
    plt.savefig(f'static/historical_plot_{symbol}_{interval}.png')


# print(plot_historical_data('BTCUSDT', '1d'))
