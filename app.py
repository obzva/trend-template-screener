import yfinance as yf
import numpy as np

# input ticker
ticker = input('which ticker do you want to search?: ')
print(f'input ticker is {ticker}')
stock = yf.Ticker(ticker)

# closing price data for one year
close_price_history = stock.history(period='1y')['Close']

# moving averages
ma_50 = close_price_history.rolling(window=50).mean()
ma_150 = close_price_history.rolling(window=150).mean()
ma_200 = close_price_history.rolling(window=200).mean()

# current values
curr_price = close_price_history[-1]
curr_ma_50 = ma_50[-1]
curr_ma_150 = ma_150[-1]
curr_ma_200 = ma_200[-1]

# 52-week(1-year) hi/lo
hi_52_week = close_price_history.max()
lo_52_week = close_price_history.min()

# 1. The current stock price is above both the 150-day (30-week) and the 200-day (40-week) moving average price lines.
def check_1() -> bool:
    message = '#1 '
    if curr_price > curr_ma_150 and curr_price > curr_ma_200:
        print(message + 'passed')
        return True
    else:
        print(message + 'failed')
        return False

# 2. The 150-day moving average is above the 200-day moving average.
def check_2() -> bool:
    message = '#2 '
    if curr_ma_150 > curr_ma_200:
        print(message + 'passed')
        return True
    else:
        print(message + 'failed')
        return False
    
# 3. The 200-day moving average line is trending up for at least 1 month (preferably 4–5 months minimum in most cases).
def check_3() -> bool:
    message = '#3 '
    ma_200_dropna = ma_200.dropna()
    if len(ma_200_dropna) < 21:
        print(message + 'not enough data to check')
        return False
    polyfit = np.polyfit(range(20), ma_200_dropna[-20:], 1)
    slope = polyfit[0]
    if slope > 0:
        print(message + 'passed')
        return True
    else:
        print(message + 'failed')
        return False
    
# 4. The 50-day (10-week) moving average is above both the 150-day and 200-day moving averages.
def check_4() -> bool:
    message = '#4 '
    if curr_ma_50 > curr_ma_150 and curr_ma_50 > curr_ma_200:
        print(message + 'passed')
        return True
    else:
        print(message + 'failed')
        return False

# 5. The current stock price is trading above the 50-day moving average.
def check_5() -> bool:
    message = '#5 '
    if curr_price > curr_ma_50:
        print(message + 'passed')
        return True
    else:
        print(message + 'failed')
        return False

# 6. The current stock price is at least 30 percent above its 52-week low. (Many of the best selections will be 100 percent, 300 percent, or greater above their 52-week low before they emerge from a solid consolidation period and mount a large scale advance.)
def check_6() -> bool:
    message = '#6 '
    if curr_price > 1.3 * lo_52_week:
        print(message + 'passed')
        return True
    else:
        print(message + 'failed')
        return False
    
# 7. The current stock price is within at least 25 percent of its 52-week high (the closer to a new high the better).
def check_7() -> bool:
    message = '#7 '
    if curr_price > 0.25 * hi_52_week:
        print(message + 'passed')
        return True
    else:
        print(message + 'failed')
        return False

check_1()
check_2()
check_3()
check_4()
check_5()
check_6()
check_7()