#!/usr/bin/env python2
import tweepy, json

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

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
	"-m",
	"--message",
	help="Message that will be posted on your timeline. Max 140 chars.",
	required=True
)

args = vars(parser.parse_args())
message = args['message']

auth = tweepy.OAuthHandler(config["twitter"]["consumer-key"], config["twitter"]["consumer-secret"])
auth.set_access_token(config["twitter"]["access-token"], config["twitter"]["access-secret"])

api = tweepy.API(auth)

twitter = Twitter(api)
twitter.tweet(message)