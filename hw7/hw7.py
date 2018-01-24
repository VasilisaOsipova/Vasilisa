# coding=utf-8
import random
def verb():
    with open ( "text1.txt", "r", encoding="utf-8") as f:  
        text = f.read()
        splited_text1 = text.split()
        return random.choice(splited_text1)   
def noun():
    with open ( "text.txt", "r", encoding="utf-8") as file:  
        text = file.read()
        splited_text = text.split()
        return random.choice(splited_text)
        
def noun1():
    with open ( "text2.txt", "r", encoding="utf-8") as file1:  
        text = file1.read()
        splited_text2 = text.split()
        return random.choice(splited_text2)
def conj():
    conjj = ["но", "а", "и"]
    return random.choice(conjj)
def conj2():
    conjj = ["когда", "что"]
    return random.choice(conjj)

def punctuation():
    marks = [".","!", "..."]
    return random.choice(marks)

def punctuation2():
    marks = [","]
    return random.choice(marks)

def verse1():
    return noun() + ' ' + verb() + ' ' + punctuation2() + ' ' + conj() + ' ' + noun1() + ' ' + verb() + punctuation()

def verse2():
    return noun() + ' ' + verb() + ' ' + punctuation2() + ' ' + conj2() + ' ' + noun1() + ' ' + verb() + punctuation()


def make_verse():
    verse = random.choice([1,2])
    if verse == 1:
        return verse1()
    else:
        return verse2()
for n in range(5):
    print(make_verse())
