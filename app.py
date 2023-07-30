import yfinance as yf

# input ticker
ticker = input('which ticker do you want to search?: ')
print(f'input ticker is {ticker}')

# 1. The current stock price is above both the 150-day (30-week) and the 200-day (40-week) moving average price lines.
stock = yf.Ticker(ticker)
close_price_history_200 = stock.history('200d')['Close']

ma_150 = close_price_history_200.rolling(150).mean()
ma_200 = close_price_history_200.rolling(200).mean()

curr_price = close_price_history_200[-1]
curr_ma_150 = ma_150[-1]
curr_ma_200 = ma_200[-1]

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