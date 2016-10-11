import tweepy
from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream

consumer_key = 'vcM8WQ6bPYZEDVhKb4LRcsQKa'
consumer_secret = '9BVC1pBjJWlKpVSN6rANNXtLWyMe6iG9QQ422HwkgmXnDAZnn7'
accest_token = '709159399294545924-FaphXT46v9wpIEMZ5qz1n9q45v4aW8c'
access_secret = 'HmsTFhgUTws3GDmHS5PrboJAvlusgQRdX9A1ilxm4FmLA'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(accest_token, access_secret)
api = tweepy.API(auth)

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('town_hall_data.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#debate'])
