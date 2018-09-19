from collections import Counter
import re


def count_frequency_words(dict):

    split_values = {key: value.strip().split(None, 50)
                    for key, value in dict.items()}

    return print(split_values)

    #word_frequency = Counter(split_values.values())
    # return print(word_frequency)
