#!/usr/bin/python3

import sys
import antigravity

def main() :
	if (len(sys.argv) == 4) :
		try : 
			lantitube = float(sys.argv[1])
		except  Exception as e :
			return print("lantitube error\n", e)
		try : 
			longitude = float(sys.argv[2])
		except  Exception as e :
			return print("longtitube error\n", e)
		try :
			datedow = bytes(sys.argv[3], 'UTF-8')
		except  Exception as e :
			return print("datedow error\n", e)
		antigravity.geohash(lantitube, longitude, datedow)
	else:
		print("put three argv this type [ex : 37.421542, -122.085589, '2005-05-26-10458.68]")


if __name__ == "__main__":
	main()