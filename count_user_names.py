""" Hvor mange forskellige brugere er der i BobRussel.txt? """

import re
import help_functions

def get_username_count(bob_ross_dict):
    regex = ', [\'\"](.*?): ' # finds the username in a line
    nameDict = help_functions.line_pattern(bob_ross_dict, regex) 
    return f'There are {len(nameDict)} diffrent users in BobRussel.txt.'
