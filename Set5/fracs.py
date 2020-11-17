import math

def lcm(x, y): #least common multiple
    return (x * y) // math.gcd(x, y)


def reduce_frac(x, y):
    d = math.gcd(x, y)
    return [x // d, y // d]


def add_frac(franc1, franc2):
    multiple = lcm(franc1[1], franc2[1]);
    numerator = int(franc1[0] * (multiple / franc1[1]) + franc2[0] * (multiple / franc2[1]))
    return reduce_frac(numerator, multiple)


def sub_frac(franc1, franc2):
    least = lcm(franc1[1], franc2[1]);
    numerator = int(franc1[0] * (least / franc1[1]) - franc2[0] * (least / franc2[1]))
    return reduce_frac(numerator, least)


def mul_frac(frac1, frac2):
    numerator = frac1[0] * frac2[0]
    denominator = frac1[1] * frac2[1]
    return reduce_frac(numerator, denominator)


def div_frac(frac1, frac2):
    numerator = frac1[0] * frac2[1]
    denominator = frac1[1] * frac2[0]
    return reduce_frac(numerator, denominator)


def is_positive(frac):
    if frac[0]>0 and frac[1] > 0 or frac[0] < 0 and frac[1] < 0:
        return True
    return False

def is_zero(frac):
    return frac[0] == 0

def cmp_frac(frac1, frac2):
    denominator = lcm(frac1[1], frac2[1])
    value1 = frac1[0] * (denominator / frac1[1])
    value2 = frac2[0] * (denominator / frac2[1])
    if value1 > value2:
        return 1
    elif value2 > value1:
        return -1
    else:
        return 0


def frac2float(frac):
    return [float(frac[0]), float(frac[1])]