import tweepy
import os

TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
TWITTER_SECRET_KEY = os.environ.get('TWITTER_SECRET_KEY')
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
TWITTER_TOKEN_SECRET = os.environ.get('TWITTER_TOKEN_SECRET')

auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_SECRET_KEY)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_TOKEN_SECRET)
api = tweepy.API(auth)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print 'Error! Failed to get request token.'

user = api.get_user('brandonfujii')
tweets = api.user_timeline('brandonfujii')

for tweet in tweets:
    print tweet.text


# userFriends = user.friends()
#
# print user.screen_name
# print user.followers_count
#
# for friend in userFriends:
#     print friend.screen_name
