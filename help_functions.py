
import re
import os
import sys
from urllib import request as req

# Returnere en dictionary baseret på en dictionary af strings
# og en regex der matcher alle eksempler på et mønster i hvert key, value par.
# Key bliver det første match i hver linje, value bliver det samlede antal af første matches


def line_pattern(string_dictionary, regex):
    pattern_dict = {}
    matches_in_line = []
    for line in list(string_dictionary.items()):
        matches_in_line = re.findall(regex, str(line))
        if len(matches_in_line) > 0:
            pattern_dict.setdefault(matches_in_line[0], 0)
            pattern_dict[matches_in_line[0]] += 1
    return pattern_dict


def download(from_url, to_file):
    if not os.path.isfile(to_file):
        req.urlretrieve(from_url, to_file)


def bob_ross_file():
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
                cfg_file = 'BobRoss.txt'
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
    return file_name


# Konveter en text fil til et dictionary.
def convert_file_dict(bob_ross_file):
    with open(bob_ross_file, encoding='utf8') as fp:
        global bob_ross_dict
        bob_ross_dict = {key: value for key, value in [
            line.strip().split(None, 1) for line in fp]}
    return bob_ross_dict
