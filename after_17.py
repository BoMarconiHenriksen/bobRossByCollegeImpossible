""" Hvor mange beskeder er der efter kl. 17:00. """

import re
import help_functions

def message_after_hour(bob_ross_dict, startHour):
    counter = 0
    hour_regex = 'T(.*?):' # finds the hours in each bob ross key: the string between the first capitalT and the first colon
    hour_dict = help_functions.line_pattern(bob_ross_dict, hour_regex)  
    for key in hour_dict:
        if int(key) >= startHour:
            counter += hour_dict[key]
    return f'There are {counter} messages after 5pm.'
