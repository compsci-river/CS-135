#
#River Sheppard
#CSI 135
#Assignment 2-1
#Password
#

import random

pinValue = 56789
pinBlank = pinValue
pinList = []

for i in range(0,5):
    pinList.append(pinBlank%10)
    pinBlank = int(pinBlank/10)

listCount = []
listRandom = []

for i in range(0,10):
    listCount.append(i)

for i in range(0,10):
    listRandom.append(random.randint(1,3))

pinString = ""
randomString = ""

for i in range(0,len(listCount)):
    pinString = pinString + str(listCount[i]) + " "

for i in range(0,len(listRandom)):
    randomString = randomString + str(listRandom[i]) + " "

convertedList = []

for i in range(0,len(pinList)):
    convertedList.append(listRandom[listCount.index(pinList[len(pinList)-(i+1)])])

randomValue = 0

for i in range(0,len(convertedList)):
    randomValue = randomValue * 10
    randomValue = randomValue + convertedList[i]

print("PIN: ", end="")
print(pinString)
print("NUM: " + randomString)
    
numInput = input("Please enter your converted password: ")

if randomValue == int(numInput):
    print("Correct")
else:
    print("Incorrect")
