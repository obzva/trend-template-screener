import yfinance as yf

# input ticker
ticker = input('which ticker do you want to search?: ')
print(f'input ticker is {ticker}')

# 1. The current stock price is above both the 150-day (30-week) and the 200-day (40-week) moving average price lines.
def check_1(ticker: str) -> bool:
    stock = yf.Ticker(ticker)
    close_price_history_200 = stock.history('200d')['Close']

    ma_150 = close_price_history_200.rolling(150).mean()
    ma_200 = close_price_history_200.rolling(200).mean()

    curr_price = close_price_history_200[-1]
    curr_ma_150 = ma_150[-1]
    curr_ma_200 = ma_200[-1]

    return curr_price > curr_ma_150 and curr_price > curr_ma_200

print('#1 ' + ('passed' if check_1(ticker) else 'failed'))