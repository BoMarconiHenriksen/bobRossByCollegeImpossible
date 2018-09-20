
import re

""" returnere en dictionary baseret på en dictionary af strings
 og en regex der matcher alle eksempler på et mønster i hvert key, value par.
 Key bliver det første match i hver linje, value bliver det samlede antal af første matches"""

def line_pattern(string_dictionary, regex):
    pattern_dict = {}
    matches_in_line = []
    for line in list(string_dictionary.items()):
        matches_in_line = re.findall(regex, str(line))
        if len(matches_in_line) > 0:
            pattern_dict.setdefault(matches_in_line[0], 0)
            pattern_dict[matches_in_line[0]] += 1
    return pattern_dict
