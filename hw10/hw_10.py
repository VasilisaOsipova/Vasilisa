#coding: utf8
import re


with open("w.txt", encoding="UTF-8") as file:
    words =file.read().replace("/n"," ")


n = len(words)

MainWords = []
k = 0


AllResults = re.findall("[а-я]*съе[а-я]*", words)
length = len(AllResults)


for i in range(2, length):
    for j in range (i, length-1):
        length = len(AllResults)
        if AllResults[i] == AllResults[j]:
            del AllResults[j]


print(AllResults)
