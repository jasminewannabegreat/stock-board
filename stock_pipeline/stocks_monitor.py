import datetime
import hashlib
import redis
import os
import sys
import json
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client
import stocks_api_client
# from cloudAMQP_client import CloudAMQPClient

SLEEP_TIME_IN_SECONDS = 3600
NEWS_TIME_OUT_IN_SECONDS = 3600 * 24 * 3

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT)
# cloudAMQP_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

STOCKS_TABLE_NAME = "stocks"
db = mongodb_client.get_db()
db[STOCKS_TABLE_NAME].drop()

STOCKS_SOURCE = []
def load_stock_symbol():
    with open('../common/nasdaq100.txt') as f:
        for line in f:
            line = line.rstrip()
            STOCKS_SOURCE.append(line)
    return STOCKS_SOURCE

# while True:                                            # we have to update stocks hourly
# STOCKS_SOURCE = load_stock_symbol()
# stocks_list = stocks_api_client.get_stock_data(STOCKS_SOURCE)
# num_of_stocks = 0

# for stock in stocks_list:
#     # stock_digest = hashlib.md5(stock['index'].encode('utf-8')).digest().encode('base64')
#     stock_digest = stock['symbol']
#     stock['digest'] = stock_digest
#     print(len(stock['history']))
#     # cloudAMQP_client.sendMessage(news)
#     # stock_json = json.dumps(stock)
#     db[STOCKS_TABLE_NAME].replace_one({'digest': stock_digest}, stock, upsert=True)
while True:
    STOCKS_SOURCE = load_stock_symbol()
    stocks_list = stocks_api_client.get_stock_data(STOCKS_SOURCE)
    num_of_stocks = 0
    for stock in stocks_list:
        num_of_stocks = num_of_stocks +1
        stock_digest = stock['symbol']
        stock['digest'] = stock_digest
        print(len(stock['history']))
        db[STOCKS_TABLE_NAME].replace_one({'digest': stock_digest}, stock, upsert=True)
    print 'Fetched %d stocks.' % num_of_stocks
    time.sleep(SLEEP_TIME_IN_SECONDS)"""update every hour"""