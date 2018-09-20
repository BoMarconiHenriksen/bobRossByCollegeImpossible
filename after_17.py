""" Hvor mange beskeder er der efter kl. 17:00. """

import re


# names_in_line = re.findall(', [\'\"](.*?): ', str(line))


def get_hour_dict(bob_ross_dict):
    nameDict = {}
    names_in_line = []

    for line in list(bob_ross_dict.items()):
        names_in_line = re.findall('T(.*?):', str(line))
        if len(names_in_line) > 0:
            nameDict.setdefault(names_in_line[0], 0)
            nameDict[names_in_line[0]] += 1
    return nameDict


def message_after_hour(bob_ross_dict, startHour):
    counter = 0
    hour_dict = get_hour_dict(bob_ross_dict)
    for key in hour_dict:
        if int(key) >= startHour:
            counter += hour_dict[key]
    return print(f'After 5pm there are {counter} messages.')
