from binance_api import download_current_prices, prepare_data

import sqlite3
from sqlite3 import OperationalError


def create_current_prices_table():
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    try:
        c.execute('CREATE TABLE current_prices (symbol, price)')
        conn.commit()
    except OperationalError:
        pass


def save_current_prices():
    current_prices_df = download_current_prices()
    create_current_prices_table()
    conn = sqlite3.connect('db.sqlite')
    result = current_prices_df.to_sql('current_prices', conn, if_exists='replace', index=False)
    return result


def print_current_prices():
    save_current_prices()
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    c.execute('''
    SELECT * FROM current_prices''')
    return c.fetchall()


def create_historical_prices_table(symbol, interval):
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    try:
        c.execute(f'CREATE TABLE {symbol}_{interval}_prices (Open time, Open, High, Low, Close, Volume)')
        conn.commit()
    except OperationalError:
        pass

def save_historical_prices(symbol, interval):
    historical_prices_df = prepare_data(symbol, interval)
    create_historical_prices_table(symbol, interval)
    conn = sqlite3.connect('db.sqlite')
    result = historical_prices_df.to_sql(f'{symbol}_{interval}_prices', conn, if_exists='replace', index=False)
    return result


def print_historical_prices(symbol, interval):
    save_historical_prices(symbol, interval)
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    c.execute(f'''
    SELECT * FROM {symbol}_{interval}_prices''')
    return c.fetchall()

# print(print_current_prices())