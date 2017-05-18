# Fundamentals of stocks using yahoo finance as data source

from yahoo_finance import Share

tickers = ['KMI', 'NNA', 'CAFD', 'GE', 'F', 'MMM', 'TXN', 'BBL', 'GLW', 'STM', 'INTC', 'QCOM']

for ticker in tickers:
    stockobj = Share(ticker)
    price = stockobj.get_price()
    bookvalue = stockobj.get_book_value()
    p_e = stockobj.get_price_earnings_ratio()
    market_cap = stockobj.get_market_cap()
    price_to_book = float(price)/float(bookvalue)

    print("\n%s" % ticker)
    print("price %.2f" % float(price))
    print("bookvalue %.2f" % float(bookvalue))
    print("price_to_book %.2f" % float(price_to_book))   
    print("P/E %.2f" % float(p_e))
    print("market cap %s" % market_cap)
