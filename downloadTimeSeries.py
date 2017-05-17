# Compatible with interpreter: Python 2.7

# Simple way to download stock time series and store them in CSV files (for further processing)

import pandas.io.data as data  # Package and modules for importing data; this code may change depending on pandas version
import datetime

def get_data(ticker):
    '''
    ticker: the ticker of the stock that is required
    parameter [to add]: time window for which data is required
    '''

    start = datetime.datetime(2016, 8, 1)
    end = datetime.date.today()

    data_ticker = data.DataReader(ticker, "yahoo", start, end)

    return data_ticker


def store_data(df_ticker, label):
    df_ticker.to_csv(label + '.csv')


if __name__ == "__main__" :

    ticker = 'XOM'

    # download data for ticker 'XOM'
    data = get_data(ticker)

    # store data in a CSV file
    store_data(data, ticker)


