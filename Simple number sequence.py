# 5 kyu  Python
# https://www.codewars.com/kata/5a28cf591f7f7019a80000de/train/python


def missing(a):
    for i in range(1, len(a)):
        b = []
        if len(a) % i == 0:
            t = i
            for i in range(0, len(a), t):
                b.append(int(a[i : i + t]))
            c = sum(b)
            d = 0
            print(b, c, b[0], b[-1], len(b))
            if b[0] + len(b) == b[-1]:
                x = int(a[0:t])
                y = int(a[-t:])
                d = int((((x + y) * (y - x + 1)) / 2) - c)
                print(x, y, d)
                return d


if __name__ == "__main__":
    t = "9899101102"
    print(missing(t))
