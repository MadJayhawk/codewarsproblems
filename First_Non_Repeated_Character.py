# 7 kyu  Python
# https://www.codewars.com/kata/570f6436b29c708a32000826/train/python
import pytest


def first_non_repeated(s):
    for i in s:
        if s.count(i) == 1:
            return i
    return None


if __name__ == "__main__":
    a = ["test", "teeter", "1122321235121222"]
    for i in a:
        print(first_non_repeated(i))
# ---------------------------------------------------------------------
# def first_non_repeated(s):
#     return next((c for c in s if s.count(c) == 1), None)
