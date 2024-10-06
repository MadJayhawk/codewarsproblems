# 6 kyu  Python
# https://www.codewars.com/kata/5f70c55c40b1c90032847588/train/python

import collections


def points(dice):
    print(dice)
    b = dict((i, dice.count(i)) for i in dice)
    if 5 in b.values():
        return 50
    if 4 in b.values():
        return 40
    if 2 in b.values() and 3 in b.values():
        return 30
    if 3 in b.values() and 2 not in b.values():
        return 0
    if 2 in b.values() and 3 not in b.values():
        return 0
    if 1 in b.values():
        if (
            sorted(dice) == list("12345")
            or sorted(dice) == list("13456")
            or sorted(dice) == list("23456")
        ):
            return 20
    return 0


"""----------------------------------------------------------------


def points(dice):
    n = len(set(dice))
    if n == 1: return 50
    if n == 2:
        a = dice.count(dice[0])
        return 30 if a == 2 or a == 3 else 40
    if n == 5:
        if set('345').issubset(set(dice)): return 20

    return 0
--------------------------------------------------------------------
def points(dice):
    if len(set(dice)) == 1: return 50
    if len(set(dice)) == 2 and (dice.count(dice[0])==4 or dice.count(dice[0])==1): return 40
    if len(set(dice)) == 2: return 30
    if len(set(dice)) == 5 and '3' in dice and '4' in dice and '5' in dice: return 20
    return 0
--------------------------------------------------------------------
"""

if __name__ == "__main__":

    x = "14325"
    print(points(x))
