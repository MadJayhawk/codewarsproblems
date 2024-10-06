# 8 kyu  Python
# https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/train/python


def two_sort(array):
    a = sorted(array)
    return "***".join(a[0])


if __name__ == "__main__":
    print(
        two_sort(
            [
                "bitcoin",
                "take",
                "over",
                "the",
                "world",
                "maybe",
                "who",
                "knows",
                "perhaps",
            ]
        )
    )
"""
--------------------------------------------------------------
def two_sort(lst):
    return '***'.join(min(lst))

Progress
Rank:5 kyu
Honor:433
Leaderboard Position:#41,573
Honor Percentile:Top 21.781%
Total Completed Kata:34
"""
