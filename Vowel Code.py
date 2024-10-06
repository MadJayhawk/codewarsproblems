# 6 kyu  Python
# https://www.codewars.com/kata/53697be005f803751e0015aa

v = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
vr = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
c = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ ?/,<.>-_=+*&^%$#@!||}{[]'


def encode(st):
    d = []
    for i in st:
        if i in c:
            d.append(i)
        else:
            d.append(str(v[i]))
    return ''.join(d)


def decode(st):
    d = []
    for i in st:
        if i in c:
            d.append(i)
        else:
            d.append(str(vr[i]))
    return ''.join(d)

if __name__ == '__main__':
    print(encode(x))

# -------------------------------------------------
CIPHER = ("aeiou", "12345")


def encode(st):
    return st.translate(str.maketrans(CIPHER[0], CIPHER[1]))


def decode(st):
    return st.translate(str.maketrans(CIPHER[1], CIPHER[0]))
