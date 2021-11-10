#!/usr/bin/python3

def number():
	r = open("numbers.txt", 'r')
	line = r.readline()
	for i in line.split(','):
		print(i.strip())
	r.close()

if __name__ == '__main__':
	number()