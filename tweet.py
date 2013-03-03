#!/usr/bin/env python2
from argparse import ArgumentParser
from controller import Controller

def get_args():
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

	return vars(parser.parse_args())

if __name__ == '__main__':
	args = get_args()
	controller = Controller()

	for key, value in args.items():
		getattr(controller, key)(value)