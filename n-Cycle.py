# 6 kyu  Python
# https://www.codewars.com/kata/5a057ec846d843c81a0000ad/train/python

import re
from decimal import Decimal, getcontext


def cycle(a):
    print(a)
    if a % 2 == 0 or a % 5 == 0:
        return -1
    if a == 3:
        return 1
    getcontext().prec = a * 2
    c = str(Decimal(1) / Decimal(a)).split(".")[1]
    ww = re.findall(re.compile(r"(0+.+?)\1+"), c)
    source = int(c)
    length = len(ww[0])
    return length


if __name__ == "__main__":
    x = 197
    print(cycle(x))
