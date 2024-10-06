# 6 kyu  Python
# https://www.codewars.com/kata/5b1cce03777ab73442000134/train/python

import math


def compare(number1, number2):
    base1, exp1 = number1
    base2, exp2 = number2
    print(base1, exp1, base2, exp2)
    a = math.log(base1) * exp1  # 2.096
    b = math.log(base2) * exp2  # 2.385
    print(a, b)
    if a > b:
        return number1
    else:
        return number2


if __name__ == "__main__":
    a = (15991, 714883)
    b = (960290, 502358)
    print(compare(a, b))

"""
------------------------------------------------------------------------------
from math import log

def compare(*numbers):
    return max(numbers, key=lambda n: n[1]*log(n[0]))

------------------------------------------------------------------------------
from math import log
def compare(n,m):
    a,b,c,d=*n,*m
    return (n,m)[d*log(c)>b*log(a)]   
"""
