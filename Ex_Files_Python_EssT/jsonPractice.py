# import pandas as pd
# import json
#
# shop = pd.read_json(r'C:\Users\h2pro\Downloads\shop.json')
#
# print(shop)
import datetime as dt
import pandas as pd
import pandas_datareader as web
from pandas_datareader import data as pdr


company = "TSLA"
start = dt.datetime(2012,1,1)
end = dt.datetime(2020,1,1)
test_start = dt.datetime(2020,1,1)
test_end = dt.datetime.now()

data = web.DataReader(company, 'yahoo', start, end)
test_data = web.DataReader(company, 'yahoo', test_start, test_end)
actual_prices = test_data ['Close'].values

# total_dataset = pd.concat((data['Close']. test_data['Close']), axis=0)

print(dt.datetime(2012,1,1))