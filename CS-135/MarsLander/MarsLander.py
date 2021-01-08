#
#River Sheppard
#CSI 135
#Assignment 4-1
#MarsLander
#py -m MarsLander level0.txt
#

import StdDraw
import StdAudio
import sys
import picture as p

velX = 0
velY = 0

fname = sys.argv[1]

with open(fname, 'r') as f:
    line = f.readline().split()
    width = int(line[0])
    height = int(line[1])
    line = f.readline().split()
    bg = p.Picture(line[0])
    line = f.readline().split()
    ship = [p.Picture(line[0]),p.Picture(line[1]),p.Picture(line[2]),p.Picture(line[3]),p.Picture(line[4]),p.Picture(line[5])]
    bottomShip = p.Picture(line[1])
    leftShip = p.Picture(line[2])
    rightShip = p.Picture(line[3])
    shipLanded = p.Picture(line[4])
    shipCrashed = p.Picture(line[5])
    line = f.readline().split()
    horiDist = int(line[0])
    vertDist = int(line[1])
    line = f.readline().split()
    shipX = float(line[0])
    shipY = float(line[1])
    line = f.readline().split()
    fuel = int(line[0])
    line = f.readline().split()
    soundOne = line[0]
    soundTwo = line[1]
    soundThree = line[2]
    line = f.readline().split()
    grav = float(line[0])
    line = f.readline().split()
    maxVel = float(line[0])
    line = f.readline().split()
    thrust = float(line[0])
    line = f.readline().split()
    padX = int(line[0])
    padWidth = int(line[1])
f.close()

StdDraw.setCanvasSize(width,height)
StdDraw.setXscale(0,width)
StdDraw.setYscale(0,height)
StdDraw.setFontFamily("SansSerif")
StdDraw.setFontSize(36)

playing = True
activeShip = ship[0]

while playing:
    StdDraw.clear()
    StdDraw.picture(bg,width/2,height/2)
    StdDraw.setPenColor(StdDraw.RED)
    StdDraw.filledRectangle(padX-padWidth,0,2*padWidth,10)
    StdDraw.picture(activeShip, shipX, shipY)
    StdDraw.setPenColor(StdDraw.GREEN)
    StdDraw.text(30,height-30,str(fuel))
    velY = velY + grav
    activeShip = ship[0]
    if StdDraw.hasNextKeyTyped():
        char = StdDraw.nextKeyTyped()
        if char == 'w' and fuel > 0:
            velY = velY + thrust
            fuel = fuel - 1
            activeShip = ship[1]
            StdAudio.playFile(soundOne)
        elif char == 'd' and fuel > 0:
            velX = velX + thrust
            fuel = fuel - 1
            activeShip = ship[2]
            StdAudio.playFile(soundOne)
        elif char == 'a' and fuel > 0:
            velX = velX - thrust
            fuel = fuel - 1
            activeShip = ship[3]
            StdAudio.playFile(soundOne)
    shipX = shipX + velX
    shipY = shipY + velY
    StdDraw.show(100)
    if shipY < vertDist:
        playing = False
        if shipX > padX-padWidth and shipX < padX+padWidth and maxVel < -1*velY:
            activeShip = ship[4]
            StdAudio.playFile(soundTwo)
        else:
            activeShip = ship[5]
            StdAudio.playFile(soundThree)
StdDraw.clear()
StdDraw.picture(bg,width/2,height/2)
StdDraw.setPenColor(StdDraw.RED)
StdDraw.filledRectangle(padX-padWidth,0,2*padWidth,10)
StdDraw.picture(activeShip, shipX, shipY)

ended = True

while ended:
    StdDraw.show(1000)
    if StdDraw.hasNextKeyTyped():
        ended = False

StdDraw.show(1000)


