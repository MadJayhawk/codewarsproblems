# 4 kyu  Python
# https://www.codewars.com/kata/ten-pin-bowling/train/python
import pytest


def bowling_score(frames):
    d = []
    sm = 0
    f = frames.split()
    for i in f:
        if "XXX" == i:
            d.append([10, 10, 10])
        elif "XX" in i:
            d.append([10, 10, int(i[-1])])
        elif "X" in i and len(i) < 3:
            d.append([10, 0])
        elif "X" in i and "/" in i:
            d.append([10, 10])
        elif "X" in i and len(i) > 2:
            d.append([10, int(i[-2]) + int(i[-1])])
        elif "/" in i and len(i) > 2:
            d.append([10, int(i[-1])])
        elif "/" in i:
            d.append([int(i[0]), 10 - int(i[0])])
        else:
            d.append([int(i[0]), int(i[1])])
    print(d)
    e = []
    for i in range(0, 9):
        # if d[i][0]==10:      # strike?
        #     if sum(d[i+1]) == 10:  # two strikes in a row?
        #         sm = 20 + d[i + 2][0]  #20 plus 1st ball in 2nd frame
        #     else:
        #         sm = sum(d[i+1])  # sum of next frame
        # elif sum(d[i]) == 10:  #spare?
        #     sm=10+d[i + 1][0]  #10 plus next ball
        # else:  # not a spare or a strike  (could be XXX, XX#,X#/,X## in 10th frame)
        #     sm=sum(d[i])

        if d[i][0] == 10:
            if d[i + 1][0] == 10:
                if i + 2 < 10:
                    sm = 20 + d[i + 2][0]
                else:
                    sm = 30
            else:
                sm = 10 + sum(d[i + 1])
        elif sum(d[i]) == 10:
            sm = 10 + d[i + 1][0]
        else:
            sm = d[i][0] + d[i][1]
        e.append(sm)
    print(e)
    return sum(e)


# s=[10,0,6,3,9,1,7,3,8,2,10,0,3,6,5,5,8,1,7,2]
# s=[[10, 0], [6, 3], [9, 1], [7, 2], [10, 0], [8, 2], [9, 0], [8, 1], [7, 3], [4, 4]]

#
if __name__ == "__main__":
    # s = 'X X 9/ 80 53 X 90 8/ X 44'
    # s = '70 80 9/ X 8/ 90 50 40 70 XX8'
    s = "X X X X X X X X X XX8"
    # assert (bowling_score(s) == 20)
    print(bowling_score(s))
