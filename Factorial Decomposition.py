# 5 kyu  Python
# https://www.codewars.com/kata/5a045fee46d843effa000070/train/python

import math


def decomp(n):
    u = math.factorial(n)
    # b = 2
    d = []
    for p in range(2, n + 1):
        isPrime = True
        for num in range(2, int(p ** 0.5) + 1):
            if p % num == 0:
                t = n / p
                isPrime = False
                break
        if isPrime:
            cnt = 0
            while u % p == 0:
                u = u // p
                cnt += 1
                if cnt == 1:
                    c = str(p)
                else:
                    c = str(p) + "^" + str(cnt)
            d.append(c)
    return " * ".join(d)


if __name__ == "__main__":
    x = 22
    print(decomp(x))
