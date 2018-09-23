"""
    Funktionen tæller, hvor mange gange ordet ruined (i diverse former) forekommer i datasættet.
"""
import help_functions


def ruin_word():
    # Bruger open() metoden til, at åbne txt filen.
    inputData = open(help_functions.get_text_file(), encoding='utf8')
    counter = 0
    for line in inputData:  # Itererer over txt filen som inputData
        # Tæller forekomster af ordet ruined (i diverse former)
        if ("Ruined" in line) or ("ruined" in line) or ("RUINED" in line):
            counter += 1
    # Printer antallet af ruined
    return f'The text file write RUINED, Ruined and ruined {counter} times.'

# Til test
# ruin_work()
