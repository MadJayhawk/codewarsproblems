# 6 kyu  Python
# https://www.codewars.com/kata/5245a9138ca049e9a10007b8
from itertools import groupby


def count_adjacent_pairs(st):
    s = st.lower().split()
    groupby(s)
    cnt = 0
    for key, group in groupby(s):
        if len(list(group)) > 1:
            cnt += 1
    return cnt


if __name__ == "__main__":
    st = "dog dog DOG dog Dog dog"
    print(count_adjacent_pairs(st))
