def ruin_word():
    inputData = open('BobRoss.txt', encoding='utf8').readlines()
    counter = 0
    for line in inputData:
        if ("Ruined" in line) or ("ruined" in line) or ("RUINED" in line):
            counter += 1
    print(f'The text file write RUINED, Ruined and ruined {counter} times.')


#ruin_work()
