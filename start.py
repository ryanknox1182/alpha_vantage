from alpha_vantage.timeseries import TimeSeries
apikey = os.environ['ALPHAVANTAGE_API_KEY']
ts = TimeSeries(key={apikey})
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL')
