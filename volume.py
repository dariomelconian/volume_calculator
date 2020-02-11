# this file is used for the designing of functions in order to compute volumes
import math

def cubeVolume(sideLength):
    volume = (sideLength * sideLength * sideLength)
    return round(volume, 2)

def pyramidVolume(b, h):
    volume = (1/3)*(b * b)*h
    return round(volume, 2)

def ellipsoidVolume(r1, r2, r3):
    volume = (4/3)*(math.pi)*r1*r2*r3
    return round(volume, 2)
