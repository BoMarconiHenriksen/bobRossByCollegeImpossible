from collections import Counter
import re


def count_frequency_words(dict):

    # return "hello count"
    chatArr = []
    stringArr = list(dict.items())
    #myarr = re.findall(':\s(.*)\'\)', str(stringArr))
    for line in stringArr:
        myarr = re.findall(':\s(.*)\'\)', str(line))
        if len(myarr) > 0:
            chatArr.append(myarr[0])
        # chatArr.append(myarr)

    wordArr = []
    for chatMessage in chatArr:
        for word in chatMessage.split():
            wordArr.append(word)

    count_words = Counter(wordArr)
    return print(f'The 20 most used words are: {count_words.most_common(20)}')
