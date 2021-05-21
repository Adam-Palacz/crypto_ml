from binance_api import download_current_prices
import sqlite3
from sqlite3 import OperationalError


def create_portfolio_table():
    portfolio_name = input('Input portfolio name: ')
    cnx = sqlite3.connect('db.sqlite')
    cursor = cnx.cursor()
    try:
        cursor.execute(f"""CREATE TABLE {portfolio_name}(
        symbol VARCHAR(10) NOT NULL UNIQUE ,
        quantity FLOAT NOT NULL,
        current_price FLOAT NOT NULL,
        fortune FLOAT NOT NULL
        )""")
        return "Table created"
    except OperationalError as err:
        return err


def print_portfolio(portfolio_name):
    cnx = sqlite3.connect('db.sqlite')
    cursor = cnx.cursor()
    try:
        cursor.execute(f'''
        SELECT * FROM {portfolio_name}''')
    except OperationalError:
        return None
    return cursor.fetchall()


def add_crypto_to_portfolio():
    portfolio_name = input("Input portfolio name: ")
    if print_portfolio(portfolio_name) is None:
        return f"No such table: {portfolio_name}"

    symbol = input("Input crypto pair: ")
    crypto_data = download_current_prices()
    selected_crypto = crypto_data.loc[crypto_data.symbol == f'{symbol}']
    if selected_crypto.empty:
        return f"No such crypto pair: {symbol}"

    try:
        quantity = float(input("Input crypto quantity: "))
    except TypeError:
        return f"Wrong quantity type"

    current_price = selected_crypto.price.iloc[0]
    fortune = round(current_price * quantity, 2)
    cnx = sqlite3.connect('db.sqlite')
    cursor = cnx.cursor()
    cursor.execute(f"""INSERT INTO {portfolio_name}(symbol, quantity, current_price, fortune)
    VALUES ('{symbol}', {quantity}, {current_price}, {fortune} )""")
    cnx.commit()
    cnx.close()
    portfolio = print_portfolio(portfolio_name)
    return portfolio
