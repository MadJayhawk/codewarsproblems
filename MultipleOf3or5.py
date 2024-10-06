# 6 kyu  Python
# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python


def solution(number):
    d = []
    if number<=0: return 0
    for i in range(1, number ):
        if i % 3 == 0:
            if i not in d:
                d.append(i)
        else:
            if i % 5 == 0:
                if i not in d:
                    d.append(i)
        # print(i, d),d[:-1]

    return sum(d)



if __name__ == "__main__":
    x = 10
    print(solution(-1))
"""   
---------------------------------------------------
    
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
    
---------------------------------------------------

def solution(number):
    sum = 0
    for i in range(number):
        if (i % 3) == 0 or (i % 5) == 0:
            sum += i
    return sum
    
----------------------------------------------------
"""
