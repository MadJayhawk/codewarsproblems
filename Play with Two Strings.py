# 5 kyu  Python
# https://www.codewars.com/kata/56c30ad8585d9ab99b000c54

def work_on_strings(a,b):
    g = [x for x in a]
    h = [x for x in b]
    for i in h:
        for index, item in enumerate(g):
            if i.lower()==item.lower():
                if item.islower():
                    g[index]=item.upper()
                else:
                    g[index]=item.lower()
    a=g
    for i in g:
        for index, item in enumerate(h):
            if i.lower()==item.lower():
                if item.islower():
                    h[index]=item.upper()
                else:
                    h[index]=item.lower()
    a+=h

    return ''.join(a)


if __name__ == '__main__':
    a = "abc"
    b = "cde"
    print(work_on_strings(a, b))
--------------------------------------------------------------------------------------------

from collections import Counter

def swap_them(a, b):
    cnt = Counter(b.lower())
    return "".join(c.swapcase() if cnt[c.lower()] % 2 else c for c in a)

def work_on_strings(a, b):
    return swap_them(a, b) + swap_them(b, a)
--------------------------------------------------------------
def work_on_strings(a, b):
    new_a = [letter if b.lower().count(letter.lower()) % 2 == 0 else letter.swapcase() for letter in a]
    new_b = [letter if a.lower().count(letter.lower()) % 2 == 0 else letter.swapcase() for letter in b]
    return ''.join(new_a) + ''.join(new_b)