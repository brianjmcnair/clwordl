#!/usr/bin/python

valid_words = open('words.txt', 'w+')
with open('/usr/share/dict/words', 'r') as file:
    for word in file.read().split():
        if len(word) == 5:
            valid_words.write(word.lower() + "\n")
file.close()
