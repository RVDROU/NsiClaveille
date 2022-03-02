import math

PI = math.pi

def rad2deg(angle) :
    return angle * 180 / PI

def deg2rad(angle) :
    return angle * PI / 180

def angle_wrap(alpha):
    return (alpha + PI) % (2 * PI) - PI
