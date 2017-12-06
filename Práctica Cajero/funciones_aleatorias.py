from random import *
from math import *

def uniforme(a: float, b: float):
    x = uniform(a, b)
    return x

def exponencial(m: float):
    y = uniform(0, 1)
    x = -1 * m * log(1 - y)
    return x

def erlang(k: int, m: float):
    x = 0.0
    me = m / k
    for i in range(k):
        x += exponencial(me)
    return x

def normal(m: float, v: float):
    total = 0.0
    for i in range(12):
        total += uniforme(0, 1)
    z = total - 6
    x = (sqrt(v) * z) + m
    return x

def geometrica(p: float):
    x = 1
    f = p
    s = f
    y = uniforme(0, 1)
    while y > s:
        f = f * (1 - p)
        s += f
        x += 1
    return x

def poisson(lam: float):
    x = 0
    f = exp(-1 * lam)
    s = f
    y = uniforme(0, 1)
    while y > s:
        f = f * lam / (x + 1)
        s += f
        x += 1
    return x

def binomial(n: int, p: float):
    x = 0
    f = exp(n * log(1 - p))
    s = f
    y = uniforme(0, 1)
    while y > s:
        f = f * p * (n - x) / ((x + 1) * (1 - p))
        s += f
        x += 1
    return x



if __name__ == '__main__':
    funcion_aleatoria()
