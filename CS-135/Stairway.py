#
#River Sheppard
#CSI 135
#Assignment 1-3
#Stairway
#

import sys

flights = int(sys.argv[1])
steps = int(sys.argv[2])
height = float(sys.argv[3])

totalSteps = flights*steps
totalHeight = totalSteps*height

print("Total steps: " + str(totalSteps))
print("Total height: " + str(totalHeight))
