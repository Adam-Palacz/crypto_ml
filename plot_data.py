from binance_api import prepare_data
import plotly.graph_objects as go
import plotly.offline as py


def print_linear(symbol, interval):
    """Plot line chart selected crypto and time interval from Binance API

    :param str symbol: crypto pair (e.g. BTCUSDT)
    :param str interval: time interval (e.g 1d, 1h, 1m.. more in README file)
    :return: html file with line chart created by plotly library
    """
    df = prepare_data(symbol, interval)
    trace = go.Ohlc(
        x=df.index[:],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name=symbol,
        increasing=dict(line=dict(color='blue')),
        decreasing=dict(line=dict(color='red')),
    )

    data = [trace]
    layout = {
        'title': symbol,
        'yaxis': {'title': 'Price'}
    }
    fig = dict(data=data, layout=layout)
    plot = py.plot(fig, filename=f'templates/{symbol}_{interval}.html', auto_open=False)
    return plot
