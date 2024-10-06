# 4 kyu  Python
# https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python

import itertools
from itertools import product


def product(lst):
    return [x for x in itertools.product(*lst)]


def get_pins(num):
    code = [int(i) for i in str(num)]
    g = {}
    g[1] = [1, 2, 4]
    g[2] = [1, 2, 3, 5]
    g[3] = [2, 3, 6]
    g[4] = [1, 4, 5, 7]
    g[5] = [2, 4, 5, 6, 8]
    g[6] = [3, 5, 6, 9]
    g[7] = [4, 7, 8]
    g[8] = [5, 7, 8, 9, 0]
    g[9] = [6, 8, 9]
    g[0] = [0, 8]
    e = []
    s = 1
    for i in code:
        e.append(g[i])

    #
    # a = [[2, 3, 6], [3, 5, 6, 9], [6, 8, 9]]

    x = product(e)

    d = []
    s = ""
    for i in x:
        for j in i:
            s += str(j)
        d.append(s)
        s = ""
    return d


if __name__ == "__main__":
    x = 11
    print(get_pins(x))

"""
-------------------------------------------------------------------------------------------------------
adjacents = {
  '1': ['2', '4'],
  '2': ['1', '5', '3'],
  '3': ['2', '6'],
  '4': ['1', '5', '7'],
  '5': ['2', '4', '6', '8'],
  '6': ['3', '5', '9'],
  '7': ['4', '8'],
  '8': ['5', '7', '9', '0'],
  '9': ['6', '8'],
  '0': ['8'],
}

def get_pins(observed):
  if len(observed) == 1:
    return adjacents[observed] + [observed]
  return [a + b for a in adjacents[observed[0]] + [observed[0]] for b in get_pins(observed[1:])]
---------------------------------------------------------------------------------------------------------
from itertools import product

PINS = {'1': '124', '2': '1253', '3': '236', '4': '1457', '5': '24568',
        '6': '3569', '7': '478', '8': '57890', '9': '689', '0': '08'}


def get_pins(observed):
    return list(map(''.join, product(*[PINS[num] for num in observed])))
"""
