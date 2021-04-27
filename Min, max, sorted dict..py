stocks = {
    'GOOG': 740.54,
    'FB': 460.64,
    'TWTR': 360.68,
    'YHOO': 215.73,
    'AAPL': 260.89
}

print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))
# If we will write stoxk.keys first then values, then it will print in alphabetical order of stocks not by value
