from math import atan2, pi

# point 1
x1 = 10
y1 = 10

# point 2
x2 = 20
y2 = 20

deltax = x2 - x1
deltay = y2 - y1

angle_rad = atan2(deltay,deltax)
angle_deg = angle_rad*180.0/pi

print(angle_deg)
