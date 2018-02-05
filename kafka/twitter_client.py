import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import argparse
import string
import json

from kafka import KafkaProducer
import time

CONSUMER_KEY = 'lWuVuekQTO6Rq6kQ0xiHV10bx'
CONSUMER_SECRET = 'X0J9bsgCdUf0ZUzbzqjLqQwwGo9Hs4fwgoAwEWHJEtSyLa2Lkk'
ACCESS_TOKEN = '958434029241450496-kO8HNHoUBvyJEVjdBnkEr2ht0wO5YoU'
ACCESS_SECRET = 'PQnCwAzW17p1uNoeaWQLYEMwxlRwzCgMi9hBHaMWZ59iI'

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def get_parser():
    """Get parser for command line arguments."""
    parser = argparse.ArgumentParser(description="Twitter Downloader")
    parser.add_argument("-q",
                        "--query",
                        dest="query",
                        help="Query/Filter",
                        default='-')
    parser.add_argument("-d",
                        "--data-dir",
                        dest="data_dir",
                        help="Output/Data Directory")
    return parser


class MyListener(StreamListener):
    """Custom StreamListener for streaming data."""

    def __init__(self, data_dir=None, query=None):
        pass
        # query_fname = format_filename(query)
        # self.outfile = "%s/stream_%s.json" % (data_dir, query_fname)

    def on_data(self, data):
        try:
            # with open(self.outfile, 'a') as f:
            #     f.write(data)
            #     print(data)
            #     return True
            print(data)
            text = data[109:data.find('source')-3]
            digist = data[60:70]
            # producer.send('AAPL', text)
            producer.send('AAPL', {'tweet': text, 'digist':digist})
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        print(status)
        return True


def format_filename(fname):
    """Convert file name into a safe string.
    Arguments:
        fname -- the file name to convert
    Return:
        String -- converted file name
    """
    return ''.join(convert_valid(one_char) for one_char in fname)


def convert_valid(one_char):
    """Convert a character into '_' if invalid.
    Arguments:
        one_char -- the char to convert
    Return:
        Character -- converted char
    """
    valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
    if one_char in valid_chars:
        return one_char
    else:
        return '_'

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

if __name__ == '__main__':
    # parser = get_parser()
    # args = parser.parse_args()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    twitter_stream = Stream(auth, MyListener())
    twitter_stream.filter(track=['AAPL'],languages=['en'])
