from math import sqrt


def score(x, y):
    distance = sqrt(x**2 + y**2)
    if min <= distance <= max:
        return 10
    if min <= distance <= max:
        return 5
    if min <= distance <= max:
        return 1
    return 0
