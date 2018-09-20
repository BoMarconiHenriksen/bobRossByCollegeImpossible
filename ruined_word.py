def ruin_work():
    inputData = open('BobRoss.txt').readlines()
    counter = 0
    for line in inputData:
        if (" Ruined " in line) or (" ruined " in line) or (" RUINED " in line):
            counter += 1
    print(counter)

ruin_work()