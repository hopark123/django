#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup


def ft_search(argv):
    url = "https://en.wikipedia.org/wiki/"
    search = argv
    i = 1
    dic = {}
    print(search)
    if search == "Philosophy" or search == "philosophy":
        print(i, "roads from", argv, "to philosophy !")
        return
    while True:
        url = "https://en.wikipedia.org/wiki/" + search
        ahtml = requests.get(url)
        soup = BeautifulSoup(ahtml.text, 'html.parser')
        text = soup.find(id='firstHeading').text
        main = soup.find("div", {"id": 'mw-content-text'})
        links = main.select('p > a')
        for link in links:
            a = link.get('href')
            if a.startswith('/wiki/') and not search.startswith('Help') or search.startswith('Wikipedia'):
                search = a.split("/")[2]
            print(search)
            i += 1
            break
        if search == "Philosophy" or search == "philosophy":
            print(i, "roads from", argv, "to philosophy !")
            return
        if not search in dic:
            dic[search] = "check"
        elif search in dic:
            print("It's a dead end !")
            break


def main():
    if (len(sys.argv) == 2):
        ft_search(sys.argv[1])
    else:
        print("input one argument")


if __name__ == '__main__':
    main()
