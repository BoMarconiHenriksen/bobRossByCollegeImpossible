"""
Beskrivelse her

Usage:
    python downloader.py [<url>] [<file_name>]
"""

import os
import sys
from datetime import datetime
import time
from urllib import request as req
import email
from collections import Counter

file_name = None


def download(from_url, to_file):
    if not os.path.isfile(to_file):
        req.urlretrieve(from_url, to_file)


if __name__ == '__main__':
    try:

        _, url, file_name = sys.argv
    except:
        try:
            _, url = sys.argv
            file_name = os.path.basename(url)
        except:
            try:

                # open file
                cfg_file = 'list_of_files.txt'
                with open(cfg_file) as fp:
                    for line in fp:
                        file_name = os.path.basename(line.rstrip())
                        url = line
                        download(url, file_name)
                sys.exit(0)
            except Exception as e:
                print(__doc__)
                sys.exit(1)
    download(url, file_name)


def convert_file_dict():
    # bob_ross_dict = {}
    with open("BobRoss.txt", encoding='utf8') as fp:  # , "r"
        global bob_ross_dict
        bob_ross_dict = {key: value for key, value in [
            line.strip().split(None, 1) for line in fp]}

        # De 2 linjer oven over erstatter nedenstående linjer.
        # for line in fp:
        #   key, value = line.strip().split(None, 1)
        #  bob_ross_dict[key] = value
    # print(bob_ross_dict)
    # print(list(bob_ross_dict.items())[1])


def messages_after_5pm():
    for key, value in bob_ross_dict.items():
        a = {}
        if key == '2015-10-29T17:00:06.067409Z':
            a[key] = value
    print(a)


convert_file_dict()
messages_after_5pm()
