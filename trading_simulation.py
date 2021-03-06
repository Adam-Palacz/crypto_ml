from predict_model import trade_move, mean_model_predict
import pandas as pd


def only_buys_simulator(symbol, interval, money):
    trade = trade_move(mean_model_predict, symbol, interval)
    money = float(money)
    money_spend = 0
    buys = 0
    bought_coins = 0
    for i in range(len(trade)):
        if trade['move'].iloc[i] == 'Buy':
            buys += 1
            bought_coins += money / trade['mean'].iloc[i]
            money_spend += money
    coin_price = trade['mean'].iloc[-1]
    fortune = (bought_coins * coin_price).round(2)
    profit = (fortune - money_spend).round(2)
    rate_of_return = ((profit / money_spend) * 100).round(2)
    buys_simulator_df = pd.DataFrame(data={
        'Buys number': buys,
        'Bought coins': bought_coins,
        'Money spend': money_spend,
        'Current coin price': coin_price,
        'Fortune': fortune,
        'Profit': profit,
        'Rate of return': rate_of_return,
    }, index=[0])
    return buys_simulator_df


def buys_sales_simulator(symbol, interval, money_buys, money_sales):
    trade = trade_move(mean_model_predict, symbol, interval)
    money_buys = float(money_buys)
    money_sales = float(money_sales)
    money_spend = 0
    buys = 0
    bought_coins = 0
    sales = 0
    for i in range(len(trade)):
        if trade['move'].iloc[i] == 'Buy':
            buys += 1
            bought_coins += money_buys / trade['mean'].iloc[i]
            money_spend += money_buys
        else:
            sales += 1
            bought_coins -= money_sales / trade['mean'].iloc[i]
            money_spend -= money_sales
    coin_price = trade['mean'].iloc[-1]
    fortune = (bought_coins * coin_price).round(2)
    profit = (fortune - money_spend).round(2)
    rate_of_return = ((profit / money_spend) * 100).round(2)
    buys_sales_simulator_df = pd.DataFrame(data={
        'Buys number': buys,
        'Sales number': sales,
        'Bought coins': bought_coins,
        'Money spend': money_spend,
        'Current coin price': coin_price,
        'Fortune': fortune,
        'Profit': profit,
        'Rate of return': rate_of_return,
    }, index=[0])
    return buys_sales_simulator_df

