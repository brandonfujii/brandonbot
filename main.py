from twitter import *
import pickle

text_file = open('tweets.txt', 'w')
pickle.dump(fetch_data('brandonfujii'), text_file);
