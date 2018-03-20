#This is a script to generate a plot
# of the past week's bitcoin prices using matplotlib
# and bitcoin-price-api.
# It creates a .png image and saves it to ../static/img/weekly_prices.png

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from .exchanges import CoinDesk

def plot_historical_price(start='2018-01-01', end=None):

    history = CoinDesk().get_historical_data_as_list(start, end)

    #only use MM-DD (by removing the year)
    x_labels = [row['date'][5:] for row in history]

    x_values = range(len(x_labels))
    y_values = [float(row['price']) for row in history]

    plt.xlabel('Date  (MM-DD)')
    plt.xticks(x_values, x_labels)
    plt.ylabel('USD Price')

    plt.plot(x_values, y_values)
