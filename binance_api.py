import requests
import pandas as pd

api_base_endpoint = "https://api.binance.com"


def download_historical_prices(symbol, interval):
    api_historical_prices = api_base_endpoint + f"/api/v3/klines?limit=1000&symbol={symbol}&interval={interval}"
    r_historical_prices = requests.get(api_historical_prices)
    historical_prices_df = pd.read_json(r_historical_prices.text)
    return historical_prices_df


def prepare_data(symbol, interval):
    historical_prices_df = download_historical_prices(symbol, interval)
    del_columns = historical_prices_df.iloc[:, 6:]
    historical_prices_df = historical_prices_df.drop(del_columns, axis=1)
    historical_prices_df = historical_prices_df.rename(columns={
        0: 'Open time', 1: 'Open', 2: 'High', 3: 'Low', 4: 'Close', 5: 'Volume'
    })
    historical_prices_df['Open time'] = pd.to_datetime(historical_prices_df['Open time'], unit="ms")
    historical_prices_df = historical_prices_df.set_index('Open time')
    return historical_prices_df


def download_current_prices():
    api_current_prices = api_base_endpoint + "/api/v3/ticker/price"
    r_current_prices = requests.get(api_current_prices)
    current_prices_df = pd.read_json(r_current_prices.text)
    return current_prices_df




# print(prepare_data('BTCUSDT', '1h'))