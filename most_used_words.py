from collections import Counter
import re

def chat_messages(dict):
    chat_list = []
    for line in list(dict.items()):
        message = re.findall(':\s(.*)\'\)', str(line)) # finds the chatmessage in a line
        if len(message) > 0:
            chat_list.append(message[0])
    return chat_list

def count_frequency_words(dict):
    all_messages = ' '.join(chat_messages(dict))
    word_list = [word for word in all_messages.split()]
    count_words = Counter(word_list)
    return f'The 20 most used words are: {count_words.most_common(20)}'
