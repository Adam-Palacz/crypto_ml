from binance_api import prepare_data
import plotly.graph_objects as go
import plotly.offline as py


def print_linear(symbol, interval):
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
    py.plot(fig, filename=f'templates/{symbol}_{interval}', auto_open=False)

