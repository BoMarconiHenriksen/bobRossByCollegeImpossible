# 2018-09-18 kl. 08.29 AM --  Christian Lykke -- usernames

import re

def get_default_line(bob_ross_dict):
    return list(bob_ross_dict.items())[1]


def get_username_count(bob_ross_dict):
    nameDict = {}
    names_in_line = []
    
    for line in list(bob_ross_dict.items()):
        names_in_line = re.findall(', [\'\"](.*?): ', str(line))
        if len(names_in_line)>0:
            nameDict.setdefault(names_in_line[0], 0)
            nameDict[names_in_line[0]] += 1
       
    return len(nameDict)