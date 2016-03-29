import tweepy, os, pickle

TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
TWITTER_SECRET_KEY = os.environ.get('TWITTER_SECRET_KEY')
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
TWITTER_TOKEN_SECRET = os.environ.get('TWITTER_TOKEN_SECRET')
TWITTER_USERNAME = 'brandonfujii'

auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_SECRET_KEY)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_TOKEN_SECRET)
api = tweepy.API(auth)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print 'Error! Failed to get request token.'

def fetch_data(user):

    timeline = api.user_timeline(user)

    tweets = []
    exclusions = ['RT', '@', 'https']

    for tweet in timeline:
        if not any(word in tweet.text for word in exclusions):
            tweets.append(tweet.text)

    return tweets


text_file = open('tweets.txt', 'w')
pickle.dump(fetch_data(TWITTER_USERNAME), text_file);
text_file.close()
