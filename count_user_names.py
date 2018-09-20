""" Hvor mange forskellige brugere er der i BobRussel.txt? """

import re


def get_username_count(bob_ross_dict):
    nameDict = {}
    names_in_line = []

    for line in list(bob_ross_dict.items()):
        # Reg ex, der finder brugeren i hver value.
        names_in_line = re.findall(', [\'\"](.*?): ', str(line))
        if len(names_in_line) > 0:
            # HVAD GØR DENNE HER LINJE OG NÆSTE?
            nameDict.setdefault(names_in_line[0], 0)
            nameDict[names_in_line[0]] += 1

    return print(f'There are {len(nameDict)} diffrent users in BobRussel.txt.')
