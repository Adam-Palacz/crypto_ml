from predict_model import trade_move, mean_model_predict


def only_buys_simulator(symbol, interval):
    trade = trade_move(mean_model_predict, symbol, interval)
    money = int(input("Input how much money do you want to spend for each transaction: "))
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
    transactions = f"""
Buys number: {buys}
Bought coins: {bought_coins}
Money spend: {money_spend}
Current coin price: {coin_price}
    """
    final_fortune = f"Fortune: {fortune}\nProfit: {profit}"
    return f"{transactions}\n{final_fortune}"


def buys_sales_simulator(symbol, interval):
    trade = trade_move(mean_model_predict, symbol, interval)
    money_buys = int(input("Input how much money do you want to spend for each transaction: "))
    money_sales = int(input("Input for how much money do you want to sell coins: "))
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
    transactions = f"""
Buys number: {buys}
Sales number: {sales}
Bought coins: {bought_coins}
Money spend: {money_spend}
Current coin price: {coin_price}
    """
    final_fortune = f"Fortune: {fortune}\nProfit: {profit}"
    return f"{transactions}\n{final_fortune}"



# print(buys_sales_simulator('BTCUSDT', '1d'))
