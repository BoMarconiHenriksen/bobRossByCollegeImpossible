"""
Beskrivelse her

Usage:
    python downloader.py [<url>] [<file_name>]
"""

import os
import sys
from urllib import request as req
import most_used_words
import after_17
import count_lines
import count_user_names



def download(from_url, to_file):
    if not os.path.isfile(to_file):
        req.urlretrieve(from_url, to_file)


if __name__ == '__main__':
    try:
        global file_name
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
    with open(file_name, encoding='utf8') as fp: 
        global bob_ross_dict
        bob_ross_dict = {key: value for key, value in [
            line.strip().split(None, 1) for line in fp]}

    # Til test
    # print(bob_ross_dict)
    # print(list(bob_ross_dict.items())[1])


convert_file_dict()
count_lines.countLines(bob_ross_dict)
print(count_user_names.get_username_count(bob_ross_dict))
print(after_17.message_after_hour(bob_ross_dict, 17))
most_used_words.count_frequency_words(bob_ross_dict)
