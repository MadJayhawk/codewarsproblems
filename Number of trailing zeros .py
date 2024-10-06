# 5 kyu  Python
# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/python


def zeros(N):
    t = 5
    a = 0
    while t <= N:
        a += N // t
        t *= 5
    return a


if __name__ == "__main__":
    print(zeros(919471640))
# ---------------------------------------------------------------------------
# Using recursion
# def zeros(n):
#   x = n/5
#   return x+zeros(x) if x else 0

# def zeros(n):
#     return n/5 + zeros(n/5) if n >= 5 else 0
