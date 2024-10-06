# 7 kyu  Python
# https://www.codewars.com/kata/57cc847e58a06b1492000264
import pytest


def sort_transform(arr):
    c = []
    b = chr(arr[0]) + chr(arr[1]) + chr(arr[-2]) + chr(arr[-1])
    c.append(b)
    a = sorted(arr, key=int)
    b = chr(a[0]) + chr(a[1]) + chr(a[-2]) + chr(a[-1])
    c.append(b)
    a = sorted(arr, key=int, reverse=True)
    b = chr(a[0]) + chr(a[1]) + chr(a[-2]) + chr(a[-1])
    c.append(b)
    d = []
    for i in arr:
        d.append(chr(i))
    a = sorted(d)
    b = a[0] + a[1] + a[-2] + a[-1]
    c.append(b)
    return "-".join(c)


if __name__ == "__main__":
    print(sort_transform([66, 101, 55, 111, 113]))
-----------------------------------------------------------------
# def extract(arr): return ''.join(arr[:2]+arr[-2:])
#
# def sort_transform(arr):
#     arr = list(map(chr,arr))
#     w1  = extract(arr)
#     arr.sort()
#     w2  = extract(arr)
#     return f'{w1}-{w2}-{w2[::-1]}-{w2}'