#
#River Sheppard
#CSI 135
#Assignment 3-2
#Lottery
#

import sys
import random

numList = [int(sys.argv[1]),int(sys.argv[2])]
checkList = [numList[0],numList[1]]
randList = [random.randint(1,10),random.randint(1,10)]
count = 0

if checkList[0] == checkList [1]:
    checkList[1] = 0

for i in range (0,len(randList)):
    for j in range (0,len(checkList)):
        if checkList[j] == randList[i]:
            count= count + 1

print("The lottery numbers were " + str(randList[0]) + " and " + str(randList[1]) + ".")
print("Your picks were " + str(numList[0]) + " and " + str(numList[1]) + ".")

if count == 0:
    print("Sorry, no match.")

if count == 1:
    print("You matched one number! You win $100!!")
if count == 2:
    print("You matched both numbers! Congratulations! You win $1000!!")
