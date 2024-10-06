# 6 kyu  Python
# https://www.codewars.com/kata/57630df805fea67b290009a3/train/python
def permutation_position(perm):
    a = "abcdefghijklmnopqrstuvwxyz"
    t = 0
    for i in range(len(perm)):
        t += a.index(perm[i]) * 26 ** (len(perm) - 1 - i)
    return t + 1
 

if __name__ == "__main__":
    print(permutation_position("foo"))
000000000000000000000000000000000000000000000000000000000000000000000000000000000


def permutation_position(x):
    return sum((ord(c) - 97) * 26 ** p for p, c in enumerate(x[::-1])) + 1

#^ Progress
# Rank:5 kyu
# Honor:433
# Leaderboard Position:#41,693
# Honor Percentile:Top 21.766%
# Total Completed Kata:38
