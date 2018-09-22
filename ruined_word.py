"""
    Funktionen tæller, hvor mange gange ordet ruined (i diverse former) forekommer i datasættet.
"""
def ruin_word():
    inputData = open('BobRoss.txt', encoding='utf8').readlines() #Bruger open() metoden til, at åbne txt filen direkte og læser derefter, hver linje
    counter = 0
    for line in inputData: #Itererer over txt filen som inputData
        if ("Ruined" in line) or ("ruined" in line) or ("RUINED" in line): #Tæller forekomster af ordet ruined (i diverse former)
            counter += 1
    print(f'The text file write RUINED, Ruined and ruined {counter} times.') #Printer antallet af ruined


#ruin_work()
