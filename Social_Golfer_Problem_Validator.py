# 4 kyu  Python
# https://www.codewars.com/kata/social-golfer-problem-validator/train/python
import pytest

def valid(s):
    # each golfer plays exactly once every day
    t=all(i.count(j)==1 for i in s for j in i)
    #  count # of groups per day - size of the groups is the same every day,
    if t==False: return False
    t = all(len(i) == len(s[0]) for i in s)
    if t==False: return False
    # unknown player in group
    d=[]
    for i in s:
        d.append(set([m for k in i for m in k]))
    for j in range(0, len(d)):
        for n in range(j, len(d)):
            if j != n:
                if d[j].difference(d[n]):
                    return False
    # count group sizes
    e = len(s[0][0])
    t = all(len(b) == e for a in s for b in a )
    if t==False: return False
    # count number of groups
    e = len(s[0])
    t = all(len(a) == e for a in s)
    if t==False: return False
    #check for empty groups
    t=all([len(j.strip()) for i in s for j in i])
    if t==False: return False
    # each player plays with every other player at most once.
    w = [b for a in s for b in a]
    for i in range(0, len(w) - 1):
        for j in range(i, len(w)):
            if i != j:
                s1 = set(w[i])
                s2 = set(w[j])
                if len(s1 & s2) > 1:
                    return False
    return t

if __name__ == '__main__':
    s = [
        ["AB", "CD", "EF", "GH"],
        ["AC", "BD", "EG", "FH"],
        ["AD", "CE","FG","BH"],
        ["AE", "BG", "CH", "FD"]]
    print(valid(s))
    s = [["AB"]]
    assert valid(s) == True
    s = [
        ["AB", "CD"],
        ["AD", "BC"],
        ["BD", "AC"]]
    assert valid(s)== True
    s = [
        ['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],
        ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
        ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],
        ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'],
        ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']]
    assert valid(s)== True
    s = [
        ["AB", "CD", "EF", "GH"],
        ["AC", "BD", "EG", "FH"],
        ["AD", "CE"],
        ["AE", "BG", "CH", "FD"]]
    assert valid(s) == False
    s = [
        ["ABC", "DEF"],
        ["ADE", "CBF"]]
    assert valid(s) == False
