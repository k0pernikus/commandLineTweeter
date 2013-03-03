#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twitter_api import Twitter
from termcolor import cprint
class Controller(object):
	def __init__(self, twitter=Twitter()):
		self.twitter = twitter

	def message(self, message):
		if message is not None and message is not "":
			self.twitter.tweet(message)
			print "I just tweeted: " + message
	def timeline(self, is_given):
		for tweet in self.twitter.get_timeline():
			cprint(tweet.user.screen_name, color="red")
			cprint(tweet.text + "\n", color="yellow")
