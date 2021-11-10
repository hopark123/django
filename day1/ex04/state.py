#!/usr/bin/python3

import sys

def find_states(cities):
	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}
	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}
	states2 = dict(map(reversed, states.items()))
	capital_cities2 = dict(map(reversed, capital_cities.items()))
	if cities in capital_cities2.keys():
		print(states2[capital_cities2[cities]])
	else:
		print("Unknown state")

def main():
	if (len(sys.argv) != 2):
		return
	else:
		find_states(sys.argv[1])

if __name__ == '__main__':
	main()