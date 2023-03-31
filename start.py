from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

apikey = os.environ['ALPHAVANTAGE_API_KEY']
ts = TimeSeries(key={apikey}, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='SPY',interval='5min', outputsize='full')
data['4. close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()
