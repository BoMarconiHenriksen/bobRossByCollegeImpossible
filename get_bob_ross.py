"""
Henter BobRoss.txt og konventer tekst filen til et dictionary.

Usage:
    python get_bob_ross.py [<url>] 
    or
    python get_bob_ross.py [<url>] [<file_name>]
"""

import os
import sys
from urllib import request as req
import most_used_words
import after_17
import count_lines
import count_user_names
import help_functions
import ruined_word


if __name__ == '__main__':
    bob_ross_file = help_functions.bob_ross_file()


bob_ross_dict = help_functions.convert_file_dict(bob_ross_file)

print(count_lines.count_lines(bob_ross_dict))
print(count_user_names.get_username_count(bob_ross_dict))
print(after_17.message_after_hour(bob_ross_dict, 17))
print(most_used_words.count_frequency_words(bob_ross_dict))
print(ruined_word.ruin_word())
