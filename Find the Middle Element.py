# 6 kyu  Python
#  https://www.codewars.com/kata/545a4c5a61aa4c6916000755
"""
As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of the numerical element that lies between the other two elements.

The input to the function will be an array of three distinct numbers (Haskell: a tuple).

For example:

gimme([2, 3, 1]) => 0
2 is the number that fits between 1 and 3 and the index of 2 in the input array is 0.
"""


def find_the_middle_element(a):
    b = {}
    for i, d in enumerate(a):
        b[d] = i
    c = sorted(b.keys())

    return b[c[1]]


print(find_the_middle_element([5, 10, 14]))
