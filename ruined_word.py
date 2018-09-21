

def ruin_work():
    inputData = open('BobRoss.txt', encoding='utf8').readlines()
    counter = 0
    for line in inputData:
        if ("Ruined" in line) or ("ruined" in line) or ("RUINED" in line):
            counter += 1
    return f'The text file write RUNIED, Ruined and ruined {counter} times.'


