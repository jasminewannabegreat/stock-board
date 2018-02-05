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

DEFAULT_SOURCE = []

def buildUrl(endpoint = STOCK_API_ENDPOINT, function = STOCK_FUNCTION):
    return endpoint + 'function=' + function


DEFAULT_SOURCE = ['AAPL','GOOGL','AMZ']

def get_stock_data(source = DEFAULT_SOURCE):
    # symbol = pd.read_csv('companylist.csv', header=None, usecols=[0])
    # print len(symbol)
    stocks_data = []
    for symbol in source:
        print symbol
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

            new_StockTwits_comments = []
            url = 'https://api.stocktwits.com/api/2/streams/symbol/{0}.json'.format(symbol)
            print(url)
            try:
                r = requests.get(url).json()
                print(len(r['messages']))
                for message in r['messages']:
                    try:
                        new_tweet = {
                            'id': message['id'], 
                            'body': message['body'], 
                            'created_at': message['created_at'],
                            'core_body': nltk_service.clean_tweet(message['body']),
                            'nltk_sentiment': nltk_service.get_tweet_sentiment(message['body']),
                            # 'azure_sentiment': azure_sentiment_service.GetSentiment(message['body'])
                        }
                        try:
                            new_tweet['azure_sentiment'] = azure_sentiment_service.GetSentiment(message['body'])
                        except Exception as e:
                            new_tweet['azure_sentiment'] = 0.5
                            print(e)
                        # print(new_tweet['azure_sentiment'])
                        new_StockTwits_comments.append(new_tweet)
                    except Exception as e:
                        print(e)
                        # pass
            except Exception as e:
                print('stock tweets part problem')
                print(e)
            # new_StockTwits_comments = [{'id': message['id'], 'body': message['body'], 'created_at': message['created_at']} for message in r['messages']]

            print(len(new_StockTwits_comments)) 

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
                'new_StockTwits_comments':new_StockTwits_comments
            }
            # print(len(history))
            if len(history) != 0:
                # f.write(stock['index']+'/n')
                stocks_data.append(stock)
        except Exception as e:
            print(e)
            pass
    print('stocks length:',len(stocks_data))
    return stocks_data
        



   

