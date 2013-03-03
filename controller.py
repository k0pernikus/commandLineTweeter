from twitter_api import Twitter
class Controller(object):
	def __init__(self, twitter=Twitter()):
		self.twitter = twitter

	def message(self, message):
		if message is not "":
			self.twitter.tweet(message)
			print "I just tweeted: " + message
	def timeline(self, is_given):
		#TODO: Print all the stream :D
		pass