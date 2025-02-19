import math
from functools import reduce

def solution(arr):
    
    return reduce(lcm, arr)

def lcm(a, b):
    return a * b // math.gcd(a, b)