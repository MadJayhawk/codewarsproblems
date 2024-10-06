# 5 kyu  Python
# https://www.codewars.com/kata/52e88b39ffb6ac53a400022e/train/python


def int32_to_ip(int32):
    if int32 == 0:
        return "0.0.0.0"
    a = format(int32, "b").zfill(32)
    print(a, len(a))
    b = []
    for i in range(0, 32, 8):
        b.append(str(int(a[i : i + 8], 2)))
    return ".".join(b)


if __name__ == "__main__":
    s = 1200947725

    print(int32_to_ip(s))
