"""
Beskrivelse her

Usage:
    python downloader.py [<url>] [<file_name>]
"""

import os
import sys
from urllib import request as req
import usernames
import after_17

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
    #bob_ross_dict = {}
    with open("BobRoss.txt", encoding='utf8') as fp:  # , "r"
        bob_ross_dict = {key: value for key, value in [
            line.split(None, 1) for line in fp]}
        # De 2 linjer oven over erstatter nedenstående linjer.
        # for line in fp:
        #   key, value = line.strip().split(None, 1)
        #  bob_ross_dict[key] = value
    # print(bob_ross_dict)
    #print(list(bob_ross_dict.items())[1])
    #print(usernames.get_username_count(bob_ross_dict))
    print(after_17.message_after_hour(bob_ross_dict, 17))

convert_file_dict()
