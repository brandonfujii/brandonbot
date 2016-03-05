from twitter import *

text_file = open('tweets.txt', 'w')
pickle.dump(tweets, text_file);
