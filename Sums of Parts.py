# 6 kyu  Python
# https://www.codewars.com/kata/5ce399e0047a45001c853c2b/train/python


def parts_sums(ls):
    d = []
    s = 00
    for i in ls[::-1]:
        d.append(s)
        s += i
    d.append(sum(ls))
    return d[::-1]


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6]
    print(parts_sums(x))
# ------------------------------------------------------------------------------
"""
def parts_sums(ls):
    result = [sum(ls)]
    for item in ls:
        result.append(result[-1]-item)
    return result
#--------------------------------------------------------
from itertools import accumulate

def parts_sums(ls):
    return [0, *accumulate(reversed(ls))][::-1]
"""
