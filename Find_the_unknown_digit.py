# 4 kyu  Python
# https://www.codewars.com/kata/find-the-unknown-digit/train/python
import re
def evaluate(x):
    v=0
    for i in range(1, len(x)):
        if not x[i].isdigit():
            a = int(x[:i])
            op = x[i]
            b = int(x[i + 1:])
            if op == '*': v = a * b
            if op == '-': v = a - b
            if op == '+': v = a + b
            # print (a,op,b)
            return v
    return -1
def solve_runes(a):
    for i in range(10):
        if str(i) not in a:
            g = re.sub('[?]', str(i), a).split('=')
            # print(g)
            h=evaluate(g[0])
            # print(h,g[0],g[1])
            if str(h)==g[1]:
                return i
    return -1

if __name__ == '__main__':
    import pytest
    assert solve_runes("1+1=?") == 2
    assert solve_runes("123*45?=5?088")== 6
    assert solve_runes("-5?*-1=5?")== 0
    assert solve_runes("19--45=5?")== -1
    assert solve_runes("??*??=302?")== 5
    assert solve_runes("?*11=??")== 2
    assert solve_runes("??*1=??")== 2

# https://www.codewars.com/kata/social-golfer-problem-validator/train/python

# print(c)
# def find_number(x,a):
#     d=[]
#     d.append(x[a])
#     for i in range(a+1,len(x)):
#         if x[i].isdigit():
#             d.append(x[i])
#         else:
#             op=x[i]
#             v=int(''.join(d))
#             return v,op,i

# def solve_runes(x):
#     return 5
    # d.append(x[0])
    # for i in range(1,len(x)):
    #     if x[i].isdigit():
    #         d.append(x[i])
    #     else:
    #         op=x[i]
    #         v=int(''.join(d))
    #         break
    # d=[]
    # w=0

    # for j in range(i+1,len(x)):
    #     if x[j].isdigit():
    #         d.append(x[j])
    #     else:
    #         w=int(''.join(d))
    #         break
    # print(v,op,w)
    # if op=='*':
    #     s=v*w
    # if op=='+':
    #     s=v+w
    # if op=='-':
    #     s=v-w
    #
    #
    # return s
