#
#River Sheppard
#CSI 135
#Assignment 3-1
#Shipping
#

import sys

weight = float(sys.argv[1])
cost = 15;

if weight > 2:
    cost = cost + 5 * (weight-2)

if weight > 70:
    cost = cost + 15;

if weight < 100:
    print("It will cost you $" + str(cost) + " to ship your package")
else:
    print("Package is over 100 pounds and cannot be shipped")
    
    
    
    
