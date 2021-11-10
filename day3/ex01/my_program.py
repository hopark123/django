#!/usr/bin/env python3

from path import Path

def main():
	folder_path = Path('.') / 'folder'
	if not folder_path.isdir() :
		folder_path.makedirs()
	f = folder_path / 'file.text'
	if not f.isfile() :
		f.touch()
	f.write_lines(["first line", "second line", "third line"])
	for line in f.lines():
		print(line.replace('\n', ''))


if __name__ == '__main__':
	main()