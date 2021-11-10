#!/usr/bin/env python3

import requests
import sys
import dewiki
import sys

class my_wiki():
    class wiki_Exception(Exception):
        def __init__(self, msg=""):
            super().__init__(msg)

    URL = 'https://en.wikipedia.org/w/api.php'
    PARAM = {
        "action": "parse",
        "prop": "wikitext",
        "format": "json",
        "redirects": "true"
    }

    def __init__(self, search=None):
        if isinstance(search, str) and not search.strip() is None:
            self.filename = "_".join(search.split()) + ".wiki"
            self.PARAM['page'] = search.lower().strip()
        else:
            raise my_wiki.wiki_Exception(
                "You must specify something to search")

    def search(self):
        res_html = requests.get(url=self.URL, params=self.PARAM)
        return res_html.json()

    def get_text(self, data):
        try:
            data = dewiki.from_string(data["parse"]["wikitext"]["*"])
            return data
        except:
            raise my_wiki.wiki_Exception("data is error")

    def make_file(self):
        try:
            data_json = self.search()
        except:
            raise my_wiki.wiki_Exception("can't search _json")
        data_string = self.get_text(data_json)
        try:
            f = open(self.filename, 'w')
        except:
            raise my_wiki.wiki_Exception("make file error")
        try:
            f.write(data_string)
        except:
            raise my_wiki.wiki_Exception("write error")
        f.close()


def main():
    if (len(sys.argv) == 2):
        try:
            wiki = my_wiki(sys.argv[1])
        except Exception as e:
            print(e)
        try:
            wiki.make_file()
        except Exception as e:
            print(e)
    else:
        print("argv error")


if __name__ == '__main__':
    main()

