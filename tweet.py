#!/usr/bin/env python2
import tweepy, json
from argparse import ArgumentParser

def init_twitter():
	auth = tweepy.OAuthHandler(config["twitter"]["consumer-key"], config["twitter"]["consumer-secret"])
	auth.set_access_token(config["twitter"]["access-token"], config["twitter"]["access-secret"])
	api = tweepy.API(auth)
	twitter = Twitter(api)

	return twitter

class argHandler(object):
	def __init__(self):
		self.api = init_twitter()
	def message(self, message):
		if message is not "":
			self.api.tweet(message)
			print "I just tweeted: " + message
	def timeline(self, is_given):
		#TODO: Print all the stream :D
		pass

try:
	with open("config.json") as config_fh:
		config = json.load(config_fh)
except IOError:
	print "Please add config file with your username and password!"

class Twitter(object):
	def __init__(self, api):
		self.api = api
	def tweet(self, message):
		self.api.update_status(message)

parser = ArgumentParser()
parser.add_argument(
	"-m",
	"--message",
	help="Message that will be posted on your timeline. Max 140 chars.",
	required=False
)

parser.add_argument(
	"-tl",
	"--timeline",
	help="Show tweets of your timeline.",
	action="store_true",
	default=False,
	required=False
)

args = vars(parser.parse_args())
argHandler = argHandler()

for key, value in args.items():
	getattr(argHandler, key)(value)