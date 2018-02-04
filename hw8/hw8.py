#coding: utf8


with open ("workfile.txt", "r", encoding = "utf-8" ) as file:
    file = file.read().replace("/n", " ").split(" ")


n = len(file)


def suffix(WorkFile):
    k = 0
    lensumm = 0
    for word in range (0, n):
        WorkString = WorkFile[word]
        if WorkString.find("ous", -3) != -1:
            k += 1
            lensumm =lensumm + len(WorkString)
    print('количество слов с суффиксом "ous"--->', k)
    z = lensumm//k
    return z


print('Средняя длинна слов с суффиксом "ous"--->', suffix(file))
