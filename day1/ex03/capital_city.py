#!/usr/bin/python3

import sys

def find_city(stat):
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
	if stat in states.keys():
		print(capital_cities[states[stat]])
	else:
		print("Unknown state")

def main():
	if (len(sys.argv) != 2):
		return
	else:
		find_city(sys.argv[1])


if __name__ == '__main__':
	main()