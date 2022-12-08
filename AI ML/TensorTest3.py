import tensorflow as tf
from tensorflow import keras
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import sys
sys.path.insert(1,'c:/Users/h2pro/Programming')
import StockPull
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Bidirectional, Dropout, Activation, Dense, LSTM
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

# function to pull stock price and volume data for a given ticker
def analysisout(tickers, period='5y', interval='1d'):
    stock = yf.Ticker(tickers)
    hist = stock.history(period, interval)
    hist.reset_index(inplace=True)
    hist = hist.rename(columns={'index': 'Date', 'Close':'Price'})
    hist = hist[['Date', 'Price', 'Volume']]
    return hist

# specify the ticker to use
tickers = 'TSLA'

# pull the stock data
data = analysisout(tickers)

# prepare the data for training
train_data = data[['Price', 'Volume']]
train_dates = pd.to_datetime(data['Date'])
scaler = StandardScaler()
scaler = scaler.fit(train_data)
train_data_scaled = scaler.transform(train_data)

# # Creating a separate scaler that works on a single column for scaling predictions
# scaler_pred = MinMaxScaler()
# df_Price = pd.DataFrame(data['Price'])
# np_Price_scaled = scaler_pred.fit_transform(df_Price)

# set up the training and test data
n_future = 1
n_past = 60

train_x = []
train_y = []

for i in range(n_past, len(train_data_scaled) - n_future +1):
    train_x.append(train_data_scaled[i - n_past:i, 0:train_data.shape[1]])
    train_y.append(train_data_scaled[i + n_future - 1:i + n_future, 0])

train_x, train_y = np.array(train_x), np.array(train_y)

# specify the test split (e.g. 0.2 for 20% of the data to be used for testing)
test_split = 0.2

# split the data into training and test sets
n_test = int(test_split * len(train_x))
test_x, test_y = train_x[:n_test], train_y[:n_test]
train_x, train_y = train_x[n_test:], train_y[n_test:]

# print the shapes of the training and test sets
print('train_x shape:', train_x.shape)
print('train_y shape:', train_y.shape)
print('test_x shape:', test_x.shape)
print('test_y shape:', test_y.shape)

# build the model
model = keras.Sequential()

model.add(keras.layers.LSTM(64, activation='relu', input_shape=(train_x.shape[1], train_x.shape[2]), return_sequences=True))
model.add(keras.layers.LSTM(32, activation='relu', return_sequences=False))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(train_y.shape[1]))

# compile the model
model.compile(optimizer='adam', loss='mse')
model.summary()

# train the model
history = model.fit(train_x, train_y, epochs=30, batch_size=32)

# evaluate the model
loss = model.evaluate(train_x, train_y)
print('Test Loss:', loss)

# make predictions on the test set
yhat = model.predict(test_x)

# add an extra dimension to the yhat array
forecast_copies = np.repeat(yhat, train_data.shape[1], axis=-1)

# invert scaling for forecast
# inv_yhat = np.concatenate((yhat, test_x[:, 1:]), axis=1)
inv_yhat = scaler.inverse_transform(forecast_copies)
inv_yhat = inv_yhat[:,0]


# add an extra dimension to the inv_y array
test_y_copies = np.repeat(test_y, train_data.shape[1], axis=-1)

# invert scaling for actual
test_y = test_y.reshape((len(test_y), 1))

# inv_y = np.concatenate((test_y, test_x[:, 1:]), axis=1)
inv_y = scaler.inverse_transform(test_y_copies)
inv_y = inv_y[:,0]

# # calculate RMSE
# rmse = np.sqrt(mean_squared_error(inv_y, inv_yhat))
# print('Test RMSE: %.3f' % rmse)

# plot the predicted and actual prices
plt.plot(inv_y, label='Actual Price')
plt.plot(inv_yhat, label='Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.title(tickers)
plt.legend()
plt.show()
