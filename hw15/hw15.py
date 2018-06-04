
import sys
import re
import string
import json

def read_file(filename):
        with open(filename,mode='r',encoding='utf-8') as file:
            lines = [line.rstrip('\n') for line in file]
            sentences = [sentence.lstrip() for line in lines for sentence in re.split('[«»\[\].!?]+',line) if len(sentence.lstrip()) > 0]
            return sentences

def get_words(sentence):
    if len(sentence) == 0:
        return []
    else:
        words = [word.strip(string.punctuation + '—') for word in sentence.split() if word.strip(string.punctuation + '—') != '']
        return words

def fifth(sentence,words):
    print("Непреобразованное предложение: {}".format(sentence))
    words_with_repeated_char = {word: {char:word.count(char) for char in word if word.count(char) > 1} for word in words}
    sentence_new = sentence
    for word_with_repeated_char, info in words_with_repeated_char.items():
        word = word_with_repeated_char
        for repeated_char, count in info.items():
            replace_char = repeated_char * count
            word_with_repeated_char = word_with_repeated_char.replace(repeated_char,replace_char)
        sentence_new = sentence_new.replace(word, word_with_repeated_char)
    print("Преобразованное предложение: {}".format(sentence_new))

if __name__=="__main__":
    sentences = read_file("test.txt")
    for sentence in sentences:
        words = get_words(sentence)
        fifth(sentence,words)
