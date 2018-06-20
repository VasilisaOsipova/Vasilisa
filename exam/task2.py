#! python3 -v
# -*- coding: utf-8 -*-
import lxml.etree as xml
import lxml.html as html
import sys
import os
import re

current_directory = os.path.dirname(__file__)
files = [file for file in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, file))]
dict_own_words = dict()
for filename in files:
    if filename.split('.')[1] in ('py','txt'):
        continue
    else:
        with open(filename, mode='r', encoding='utf-8') as file:
            lines = file.read().encode()
            tree = xml.fromstring(lines)
            for elem in tree.iter():
                if elem.tag == 'ana':
                    if elem.attrib['lex'].istitle():
                        if elem.attrib['lex'] not in dict_own_words:
                            dict_own_words[elem.attrib['lex']] = 1
                        else:
                            dict_own_words[elem.attrib['lex']] += 1
for own_word in dict_own_words.keys():
    print("{word}\t{count}".format(word=own_word, count=dict_own_words[own_word]))