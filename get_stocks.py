from stocksymbol import StockSymbol

api_key = 'a029be3d-323a-41d7-90b1-c563780246f7'
ss = StockSymbol(api_key)

symbol_list_us = ss.get_symbol_list(market='US', symbols_only=True)

joined_list = ','.join(symbol_list_us)

with open('us_symbols.txt', 'w') as f:
    f.write(joined_list)

print('Done!')