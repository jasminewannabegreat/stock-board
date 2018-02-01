from json import loads
import requests
import time
import pandas as pd

"""GET STOCK DATA FROM ALPHA VANTAGE"""
STOCK_API_ENDPOINT = 'https://www.alphavantage.co/query?'
STOCK_API_KEY = 'A4CE10H2F8BO365X'
STOCK_FUNCTION = 'TIME_SERIES_DAILY'

"""GET YEARLY DATA FROM IEX ENDPOINT"""
IEX_STOCK_ENDPOINT = 'https://api.iextrading.com/1.0/stock/'

def buildUrl(endpoint = STOCK_API_ENDPOINT, function = STOCK_FUNCTION):
    return endpoint + 'function=' + function

def load_stock_symbol():
    data = []
    with open('nasdaq100.txt') as f:
        for line in f:
            line = line.rstrip()
            data.append(line)
    return data

def get_stock_data():
    # symbol = pd.read_csv('companylist.csv', header=None, usecols=[0])
    # print len(symbol)
    stocks_data = []
    symbol_list = load_stock_symbol()
    for symbol in symbol_list:
        # print symbol
        # payload = {'function':STOCK_FUNCTION,
        #            'symbol':symbol,
        #            'apikey':STOCK_API_KEY}
        # response = requests.get(STOCK_API_ENDPOINT, params = payload)

        #GET today's quote
        try:
            quote = IEX_STOCK_ENDPOINT + symbol + '/quote'
            today = requests.get(quote)
            today_json = loads(today.content)

            #get history's quote
            url = IEX_STOCK_ENDPOINT + symbol + '/chart/1y'
            response  = requests.get(url)
            content = response.content
            res_json = loads(content)
            history = []
            if res_json is not None:
                history.extend(res_json)

            stock = {
                'symbol': symbol,
                'open': today_json['open'],
                'close': today_json['close'],
                'change':today_json['change'],
                'percent_change':today_json['changePercent'],
                'prev_close':today_json['previousClose'],
                'price':today_json['latestPrice'],
                'volume':today_json['latestVolume'],
                'history':history
                # 'new_StockTwits_comments':new_StockTwits_comments
            }
            print(len(history))
            if len(history) != 0:
                # f.write(stock['index']+'/n')
                stocks_data.append(stock)
        except Exception as e:
            print(e)
            pass
    print('stocks length:',len(stocks_data))
    return stocks_data
        



   

