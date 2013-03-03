#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, tweepy
class Twitter(object):
	def __init__(self):
		try:
			with open("config.json") as config_fh:
				config = json.load(config_fh)
		except IOError:
			print "Please add config file with your username and password!"

		auth = tweepy.OAuthHandler(config["twitter"]["consumer-key"], config["twitter"]["consumer-secret"])
		auth.set_access_token(config["twitter"]["access-token"], config["twitter"]["access-secret"])
		self.api  = tweepy.API(auth)

	def tweet(self, message):
		self.api.update_status(message)

	def get_timeline(self):
		return self.api.home_timeline()