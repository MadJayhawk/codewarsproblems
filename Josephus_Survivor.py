# 5 kyu  Python
# https://www.codewars.com/kata/josephus-survivor/python


def josephus_survivor(n, k):
    v = 0
    for i in range(1, n + 1):
        v = (v + k) % i
    return v + 1


if __name__ == "__main__":
    print(josephus_survivor(7, 3))
