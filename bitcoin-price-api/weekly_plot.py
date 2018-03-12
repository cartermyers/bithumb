#This is a script to generate a plot
# of the past week's bitcoin prices using matplotlib
# and bitcoin-price-api.
# It creates a .png image and saves it to ../static/img/weekly_prices.png

import matplotlib.pyplot as plt
from exchanges import CoinDesk

def plot_historical_price(start='2018-01-01', end=None):
    history = CoinDesk().get_historical_data_as_dict(start, end)

    #only use MM-DD (by removing the year)
    x_labels =[date[5:] for date in history.keys()]

    x_values = range(len(x_labels))
    y_values = history.values()

    plt.xlabel('Date  (MM-DD)')
    plt.xticks(x_values, x_labels)
    plt.ylabel('USD Price')

    plt.plot(x_values, y_values)



if __name__ == "__main__":
    from datetime import datetime, timedelta

    #get the start of last week (in YYYY-MM-DD format; UTC timezone)
    # that is, today - 7 days
    last_week = datetime.now() - timedelta(days=7)
    last_week = '{}-{:02d}-{:02d}'.format(last_week.year, last_week.month, last_week.day)

    #plot the graph starting from last week
    plot_historical_price(last_week)

    #change the size:
    plt.rcParams['figure.figsize'] = [30, 30]
    plt.tight_layout()
    #and save that to an image
    plt.savefig('../static/img/weekly_prices.png')
