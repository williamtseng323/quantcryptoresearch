import pandas as pd
import numpy as np
from ta.trend import ADXIndicator
from ta.volatility import BollingerBands
import yfinance as yf
# Assuming df is your DataFrame and it has columns: 'Open', 'High', 'Low', 'Close'
df = yf.download("BTC-USD",start="2020-01-01",end="2023-11-18")

# 1. Support and Resistance Levels
df['Support'] = df['Low'].rolling(window=80).min()
df['Resistance'] = df['High'].rolling(window=80).max()

# 2. Trend Direction
# Using the ADX indicator. ADX > 25 indicates a strong trend.
adxI = ADXIndicator(df['High'], df['Low'], df['Close'], window=14)
df['Trend_Strength_ADX'] = adxI.adx()
df['Trend_Direction'] = np.where(df['Trend_Strength_ADX'] > 25, np.where(df['Close'].diff() >= 0, 1, -1), 0)

# 3. Your custom technical indicators
# df['Your_Indicator1'] = ...
# df['Your_Indicator2'] = ...
# df['Your_Indicator3'] = ...
# df['Your_Indicator4'] = ...
# df['Your_Indicator5'] = ...

# 4. Bollinger Bands
bollinger = BollingerBands(df['Close'], window=20, window_dev=2)
df['Bollinger_Lower'] = bollinger.bollinger_lband()  # -2 sd
df['Bollinger_Upper'] = bollinger.bollinger_hband()  # 2 sd

df.to_csv("JJ.csv")