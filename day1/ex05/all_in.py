#!/usr/bin/python3

import sys

def check_argv(str):
	states = {
	"Oregon": "OR",
	"Alabama": "AL",
	"New Jersey": "NJ",
	"Colorado": "CO"
	}
	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}
	states2 = dict(map(reversed, states.items()))
	capital_cities2 = dict(map(reversed, capital_cities.items()))
	str2 = str.strip()
	if (str2 == ''):
		return
	if str2.title() in states.keys():
		print(capital_cities[states[str2.title()]],
				"is the capital of", str2.title())
	elif str2.title() in capital_cities2.keys():
		print(str2.title(), "is the capital of",
				states2[capital_cities2[str2.title()]])
	else:
		print(str2, "is neither a capital city nor a state")

def main():
	if (len(sys.argv) != 2):
		return
	else:
		str = sys.argv[1].split(',')
		for i in str:
			check_argv(i)

if __name__ == '__main__':
	main()
