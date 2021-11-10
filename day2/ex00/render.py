#!/usr/bin/python3

import sys, os, re
import settings

def main():
	if (len(sys.argv) != 2):
		return print("not invaild argv")
	path = sys.argv[1]
	if re.match("^.+\\.template$", path) is None :
		return print("put [*.template] file")
	if os.path.isfile(path) == False :
		return print("not exist file")
	f = open(path, mode="r", encoding='utf-8')
	template = "".join(f.readlines())
	file = template.format(title = settings.title, name = settings.name, surname = settings.surname, age = settings.age, profession = settings.profession)
	f.close()
	path = re.sub(".template$", ".html", path)
	f = open(path, mode="w", encoding='utf-8')
	f.write(file)
	f.close()
if __name__ == '__main__' :
	main()