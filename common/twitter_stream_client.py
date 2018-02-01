import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import argparse
import string
import json

CONSUMER_KEY = 'lWuVuekQTO6Rq6kQ0xiHV10bx'
CONSUMER_SECRET = 'X0J9bsgCdUf0ZUzbzqjLqQwwGo9Hs4fwgoAwEWHJEtSyLa2Lkk'
ACCESS_TOKEN = '958434029241450496-kO8HNHoUBvyJEVjdBnkEr2ht0wO5YoU'
ACCESS_SECRET = 'PQnCwAzW17p1uNoeaWQLYEMwxlRwzCgMi9hBHaMWZ59iI'

filter = ''
# def get_Auth():
#     with open('credentials.txt','r') as file:
#         for line in file:
#             line = line.rstrip()
#             if line.startswith('consumer_key'):
#                 CONSUMER_KEY = line[line.index('=')+1:]
#                 print CONSUMER_KEY
#             elif line.startswith('comsumer_secret'):
#                 CONSUMER_SECRET = line[line.index('=')+1:]
#                 print CONSUMER_SECRET
#             elif line.startswith('access_token'):
#                 ACCESS_SECRET = line[line.index('=')+1:]
#                 print ACCESS_SECRET
#             else:
#                 ACCESS_TOKEN = line[line.index('=')+1:]
#                 print ACCESS_TOKEN
# def get_parser():
#     """Get parser for command line arguments."""
#     parser = argparse.ArgumentParser(description="Twitter Downloader")
#     parser.add_argument("-q",
#                         "--query",
#                         dest="query",
#                         help="Query/Filter",
#                         default='-')
#     parser.add_argument("-d",
#                         "--data-dir",
#                         dest="data_dir",
#                         help="Output/Data Directory")
#     return parser

# start_time = time.time()
class myStreamListener(StreamListener):
    """Custom StreamListener for streaming data."""
    # def __init__(self, start_time, time_limit=60):

    #     self.time = start_time
    #     self.limit = time_limit

    def on_data(self, data):
        print(data)
        try:
            file_path = 'twitter_stream_data/twitter_' + filter +'.json'
            with open(file_path, 'a+') as f:
                f.write(data)
                print(data)
                return True
        except BaseException as e:
            print("Error on data", e)
        return True
#     def __init__(self, data_dir, query):
#         query_fname = format_filename(query)
#         self.outfile = "%s/stream_%s.json" % (data_dir, query_fname)

#     def on_data(self, data):
#         try:
#             with open(self.outfile, 'a') as f:
#                 f.write(data)
#                 print(data)
#                 return True
#         except BaseException as e:
#             print("Error on_data: %s" % str(e))
#             time.sleep(5)
#         return True

    def on_error(self, status):
        print(status)


# def format_filename(fname):
#     """Convert file name into a safe string.
#     Arguments:
#         fname -- the file name to convert
#     Return:
#         String -- converted file name
#     """
#     return ''.join(convert_valid(one_char) for one_char in fname)


# def convert_valid(one_char):
#     """Convert a character into '_' if invalid.
#     Arguments:
#         one_char -- the char to convert
#     Return:
#         Character -- converted char
#     """
#     valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
#     if one_char in valid_chars:
#         return one_char
#     else:
#         return '_'

# @classmethod
# def parse(cls, api, raw):
#     status = cls.first_parse(api, raw)
#     setattr(status, 'json', json.dumps(raw))
#     return status

# if __name__ == '__main__':
#     parser = get_parser()
#     args = parser.parse_args()
#     auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
#     auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
#     api = tweepy.API(auth)

#     twitter_stream = Stream(auth, myStreamListener(args.data_dir, args.query))
#     twitter_stream.filter(track=[args.query])

    
if __name__== '__main__':
    # get_Auth()
    filter = 'AAPL'
    auth =  OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    myStreamListener = myStreamListener()
    myStream = tweepy.Stream(auth, myStreamListener)
    myStream.filter(track=[filter])
# # python twitter_stream_download.py -q AAPL -d data