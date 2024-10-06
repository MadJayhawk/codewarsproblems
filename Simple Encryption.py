# 6 kyu  Python
# https://www.codewars.com/kata/57814d79a56c88e3e0000786


def encrypt(text, n):
    for k in range(n):
        d = []
        e = []
        for i, j in enumerate(text):
            d.append(j) if i % 2 != 0 else e.append(j)
        text = "".join(d) + "".join(e)
    return text


def decrypt(encrypted_text, n):
    for k in range(n):
        b = len(encrypted_text) // 2
        d = []
        for i in range(int(b)):
            d.append(encrypted_text[b:][i])
            d.append(encrypted_text[:b][i])
        if b * 2 < len(encrypted_text):
            d.append(encrypted_text[-1])
        encrypted_text = "".join(d)
    return encrypted_text


if __name__ == "__main__":
    print(decrypt("hsi  etTi sats!", 1))
-------------------------------------------------------------------------------


def decrypt(text, n):
    if text in ("", None):
        return text

    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i + 1] + a[i:i + 1] for i in range(ndx + 1))
    return text


def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text


Progress
Rank:5 kyu
Honor:441
Leaderboard Position:#40,702
Honor Percentile:Top 21.243%
Total Completed Kata:38
