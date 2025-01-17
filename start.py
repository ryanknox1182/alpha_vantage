import matplotlib
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key='QUE4JESTDHAN1V5N', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='SPY',interval='5min', outputsize='full')
data['4. close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()
