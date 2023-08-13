import yfinance as yf
import json
from tqdm import tqdm

with open('us_symbols.txt', 'r') as file:
    content = file.read()
    tickers = content.strip().split(',')

def IBD_style_RS(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        history = stock.history(period="1y")

        current = history['Close'].iloc[-1]

        before63 = history['Close'].iloc[-64]
        before126 = history['Close'].iloc[-127]
        before189 = history['Close'].iloc[-190]
        before252 = history['Close'].iloc[0]

        relative_strength = (2 * current/before63) + (current/before126) + (current/before189) + (current/before252)

        return {"relative_strength": relative_strength}

    except Exception as e:
        return {"relative_strength": 0}

RS_dict = {ticker: IBD_style_RS(ticker) for ticker in tqdm(tickers, desc="Processing tickers")}

print(json.dumps(RS_dict, indent=4))
