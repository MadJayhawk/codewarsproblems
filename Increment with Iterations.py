# 5 kyu  Python
# https://www.codewars.com/kata/5ecc16daa200d2000165c5b1/train/python

#
# def increment(number, iterations, spacer):
#     return
#
#
# if __name__ == "__main__":
#     number = 123
#     iterations = 5
#     spacer = 2
#     print(increment(number, iterations, spacer))
#     -----------------------------------------------------------


def increment(number, iterations, spacer):
    step = len(str(number)) - 1

    for i in range(iterations):
        step = (step - spacer) % len(str(number))
        number = number + 10 ** (step)

        return number


if __name__ == "__main__":
    number = 123
    iterations = 5
    spacer = 2
    print(increment(number, iterations, spacer))
----------------------------------------------------------------------------
def increment(number, iterations, spacer):
    pos = 0
    for _ in range(iterations):
        s = str(number)
        pos = (pos + spacer) % len(s)
        number += 10 ** (len(s) - 1 - pos)
        pos += len(s) != len(str(number))
    return number
------------------------------------------------------------------------
def increment(number, iterations, spacer):
    pos, number = -1, dict(enumerate(map(int, str(number)[::-1])))
    for _ in range(iterations):
        ptr = pos = (pos - spacer) % len(number)
        while True:
            carry, number[ptr] = divmod(number.get(ptr, 0) + 1, 10)
            if not carry: break
            ptr += 1
    return int(''.join(map(str, number.values()))[::-1])