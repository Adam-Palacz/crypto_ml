import datetime
import pandas as pd
import requests

api_base_endpoint = "https://api.binance.com"


def download_historical_prices(symbol, interval):
    api_historical_prices = api_base_endpoint + f"/api/v3/klines?limit=1000&symbol={symbol}&interval={interval}"
    r_historical_prices = requests.get(api_historical_prices)
    try:
        historical_prices_df = pd.read_json(r_historical_prices.text)
        return historical_prices_df
    except ValueError:
        return None


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


def current_time():
    result = datetime.datetime.now().strftime("%Y_%b_%d_%H:%M")
    return result


def save_current_prices():
    time_now = current_time()
    download_current_prices().to_csv(f'data/crypto_prices_{time_now}')
    return "Data saved"


def save_historical_prices(symbol, interval):
    if download_historical_prices(symbol, interval) is None:
        return "Wrong data"
    data = prepare_data(symbol, interval)
    time_now = current_time()
    data.to_csv(f'data/{symbol}_{interval}_prices_{time_now}')
    return "Data saved"
