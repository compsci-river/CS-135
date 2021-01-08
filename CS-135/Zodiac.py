#
#River Sheppard
#CSI 135
#Assignment 3-3
#Zodiac
#

import sys

birthYear = int(sys.argv[1])
rem = birthYear%12
years = ["Monkey","Rooster","Dog","Pig","Rat","Ox","Tiger","Rabbit","Dragon","Snake","Horse","Sheep"]
year = years[rem]

print("You were born in the year of the\n" + year +".")
