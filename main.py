import finplot as fplt
# import yfinance
import pandas as pd

# df = yfinance.download('AAPL')
# df = pd.read_csv("ibov2000-2020.csv")
# candles = df[['Date','Open','High','Low','Close']]
# fplt.candlestick_ochl(candles)
# fplt.show()

df = fplt.pd.read_csv('ibov2000-2020.csv', parse_dates=['Date'], index_col='Date').sort_index()
fplt.candlestick_ochl(df[['Open','Close','High','Low']])
fplt.show()