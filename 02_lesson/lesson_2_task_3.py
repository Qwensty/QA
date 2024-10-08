import math


def square(side):
    area = side*side
    return math.ceil(area)


side = 43.55
area = square(side)


print(f"Площадь квадрата со стороной {side} равна {area}")
