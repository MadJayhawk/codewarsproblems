# 8 kyu  Python
# https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python

def areYouPlayingBanjo(name):
    if name[0].upper() == "D":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


if __name__ == "__main__":
    print(areYouPlayingBanjo("Dennis"))

---------------------------------------------------------------------------

def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo";

Progress
Rank:5 kyu
Honor:431
Leaderboard Position:#41,828
Honor Percentile:Top 21.915%
Total Completed Kata:34