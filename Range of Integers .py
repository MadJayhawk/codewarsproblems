# 5 kyu  Python
# https://www.codewars.com/kata/5b6b67a5ecd0979e5b00000e/train/python


def mystery_range(s, n):
    k = len(s) / n
    print(n, k, len(s) % n)
    print(s)
    if "100" in s:
        for i in range(100, 200):
            if s.find(str(i)) == -1:
                return [i - n, i - 1]
    elif "10" in s and k != 2.0:
        return [10 - (n - len(s) % n), 10 + len(s) % n - 1]

    elif k == 1.0:
        t = sorted(s)
        return [t[0], t[-1]]
    elif k == 2.0:
        t = []
        for i in range(0, len(s), 2):
            t.append(s[i] + s[i + 1])
        r = sorted(t)
        return [int(r[0]), int(r[-1])]
    elif k == 3.0:
        t = []
        for i in range(0, len(s), 3):
            t.append(s[i] + s[i + 1] + s[i + 2])
        r = sorted(t)
        return [int(r[0]), int(r[-1])]


if __name__ == "__main__":
    x = "57755488799715021391892385890806723998334829144102629487228476633166132968378752953170191017641156224494559636997514311818440463689304227931374100687753602278209412179814735665358564258655"
    m = 94
    print(mystery_range(x, m))
