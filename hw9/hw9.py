#coding: utf8
import random


MainDict = {}


with open("MainDict.txt", encoding="UTF-8") as file:
    for line in file:
        key, *value = line.split()
        MainDict[key] = value



del MainDict['\ufeff']


def GetKey(dict):
    MainKey = dict.keys()
    return MainKey


KeyList = GetKey(MainDict)
KeyList = list(KeyList)
n = len( KeyList )



def RandomKey (list, length ):
    RandKeyNum = random.randint(0, length)
    RandKey = list[RandKeyNum]
    RandKeyValues = MainDict.get( RandKey )
    RandValue = random.choice( RandKeyValues )
    return RandValue


tryes = 1
ChosenValue = RandomKey(KeyList, n-1)
print (ChosenValue)
while True:
    UserInput = input()
    for i in range (0, n-1):
        if UserInput == KeyList[i]:
            CheckList = MainDict[KeyList[i]]
            for j in range (0, n-1):
                if ChosenValue == CheckList[j]:
                    print("Right, number of tryes--->", tryes )
                    exit()
    tryes += 1