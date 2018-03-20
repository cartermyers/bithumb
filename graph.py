import matplotlib
matplotlib.use('Agg')

from datetime import datetime, timedelta
import matplotlib.pyplot as plt

from bitcoin_price_api.plot_graph import plot_historical_price


#first, set the size of the graph
plt.rcParams['figure.figsize'] = [13, 7.5]

#get the start of last week (in YYYY-MM-DD format; UTC timezone)
# that is, today - 7 days
last_week = datetime.now() - timedelta(days=7)
last_week = '{}-{:02d}-{:02d}'.format(last_week.year, last_week.month, last_week.day)

#plot the graph starting from last week
plot_historical_price(last_week)

#and save that to an image
plt.tight_layout()
plt.savefig('/home/shin202j/bithumb/static/img/weekly_prices.png', format='png')
