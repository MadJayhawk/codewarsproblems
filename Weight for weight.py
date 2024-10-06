# 5 kyu  Python
# https://www.codewars.com/kata/55c6126177c9441a570000cc


def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r


def order_weight(wts):
    b = list(map(int, wts.split()))
    a = []
    for i in b:
        s = sum_digits(i)
        a.append([s, str(i)])
    d = sorted(sorted(a, key=lambda x: x[1]))
    s = " ".join(str(x[1]) for x in d)
    return s


if __name__ == "__main__":
    print(
        order_weight(
            "1 2 200 4 4 6 6 7 7 9 18 27 72 81 91 425 31064 7920 67407 96488 34608557 71899703"
        )
    )
----------------------------------------------------------------------------

def order_weight(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))

----------------------------------------------------------------------------


def sum_string(s):
    sum = 0
    for digit in s:
        sum += int(digit)
    return sum


def order_weight(strng):
    # your code
    initial_list = sorted(strng.split())
    result = " ".join(sorted(initial_list, key=sum_string))

    return result