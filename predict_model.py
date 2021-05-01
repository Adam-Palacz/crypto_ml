from sklearn.linear_model import LinearRegression
import numpy as np
from binance_api import prepare_data


def close_model_prepare(symbol, interval):
    close_predict = prepare_data(symbol, interval)
    close_predict['close_3'] = close_predict['Close'].rolling(window=3).mean()
    close_predict['close_9'] = close_predict['Close'].rolling(window=9).mean()
    close_predict['next_day_close_price'] = close_predict['Close'].shift(-1)
    close_predict = close_predict.dropna()
    return close_predict


def close_model_train(symbol, interval):
    close_predict = close_model_prepare(symbol, interval)
    X = close_predict[['close_3', 'close_9']]
    y = close_predict['next_day_close_price']
    split = split_data(close_predict)
    X_train = X[:split]
    y_train = y[:split]
    model = train_model(X_train, y_train)
    return model


def split_data(data_frame):
    split_size = 0.8
    split_size = int(split_size * (len(data_frame)))
    return split_size


def train_model(X_train, Y_train):
    model = LinearRegression()
    trained_model = model.fit(X_train, Y_train)
    return trained_model


def close_model_predict(symbol, interval):
    close_predict = close_model_prepare(symbol, interval)
    model = close_model_train(symbol, interval)
    close_predict = close_predict.drop('next_day_close_price', axis=1)
    close_predict['predicted_price'] = model.predict(close_predict[['close_3', 'close_9']])
    return close_predict.tail()


def trade_move(function, symbol, interval):
    predicted = function(symbol, interval)
    predicted['move'] = np.where(predicted['predicted_price'].shift(1) < predicted['predicted_price'], "Buy", "Stay")
    return predicted


def mean_model_prepare(symbol, interval):
    mean_predict = prepare_data(symbol, interval)
    mean_predict = mean_predict.iloc[:, 0:4].copy()
    mean_predict['mean'] = 0
    for i in range(len(mean_predict)):
        mean_predict['mean'].iloc[i] = mean_predict.iloc[i, :4].mean()
    return mean_predict


def mean_model_train(symbol, interval):
    mean_predict = mean_model_prepare(symbol, interval)
    mean_predict['next_day_close_price'] = mean_predict['mean'].shift(-1)
    mean_predict = mean_predict.dropna()
    X = mean_predict[['Open', 'High', 'Low', 'Close']]
    y = mean_predict['next_day_close_price']
    split = split_data(mean_predict)
    X_train = X[:split]
    y_train = y[:split]
    model = train_model(X_train, y_train)
    return model


def mean_model_predict(symbol, interval):
    mean_predict = mean_model_prepare(symbol, interval)
    model = mean_model_train(symbol, interval)
    mean_predict['predicted_price'] = model.predict(mean_predict[['Open', 'High', 'Low', 'Close']])
    return mean_predict




