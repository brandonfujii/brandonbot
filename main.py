#!/usr/bin/python

import sys
from twitter import *

def main():
	if len(sys.argv) != 2:
		print "usage: ./main.py --twitbot"
		sys.exit(1)

	option = sys.argv[1]

	if option == '--twitbot':
		fetch_data(TWITTER_USERNAME)
		text_file = open('tweets.txt', 'w')
		pickle.dump(fetch_data(TWITTER_USERNAME), text_file);
		text_file.close()


if __name__ == '__main__':
  main()