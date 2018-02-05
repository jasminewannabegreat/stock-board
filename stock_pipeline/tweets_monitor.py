import datetime
import hashlib
import redis
import os
import sys
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client
import stocks_api_client
import twitter_stream_client
# from cloudAMQP_client import CloudAMQPClient

SLEEP_TIME_IN_SECONDS = 10
NEWS_TIME_OUT_IN_SECONDS = 3600 * 24 * 3

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT)
# cloudAMQP_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

STOCKS_TABLE_NAME = "stock"
db = mongodb_client.get_db()


# while True:                                            # we have to update stocks hourly
stocks_list = stocks_api_client.get_stock_data()
num_of_stocks = 0
#This file is never used
for stock in stocks_list:
    # stock_digest = hashlib.md5(stock['index'].encode('utf-8')).digest().encode('base64')
    stock_digest = stock['symbol']
    stock['digest'] = stock_digest
    ''' redis can dedupe here '''
    print(len(stock['history']))
    # cloudAMQP_client.sendMessage(news)
    # stock_json = json.dumps(stock)
    db[STOCKS_TABLE_NAME].replace_one({'digest': stock_digest}, stock, upsert=True)