import math


def roundup(a, digits=0):
    n = 10**-digits
    return round(math.ceil(a / n) * n, digits)
