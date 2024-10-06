# 5 kyu  Python
# file namehttps://www.codewars.com/kata/52774a314c2333f0a7000688/train/python


def valid_parenthesess(a):
    cnt = 0
    i = 0
    while cnt >= 0 and i < len(a):
        if a[i] == "(":
            cnt += 1
        else:
            if a[i] == ")":
                cnt -= 1
        i += 1
    if cnt == 0:
        return "True"
    else:
        return "False"


if __name__ == "__main__":
    x = ")(()))"
    print(valid_parenthesess(x))
"""
----------------------------------------------------------------------------------
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False
-----------------------------------------------------------------------------------
iparens = iter('(){}[]<>')
parens = dict(zip(iparens, iparens))
closing = parens.values()

def valid_parentheses(astr):
    stack = []
    for c in astr:
        d = parens.get(c, None)
        if d:
            stack.append(d)
        elif c in closing:
            if not stack or c != stack.pop():
                return False
    return not stack
-----------------------------------------------------------------------------------
import re

def valid_parentheses(s):
    try:
        re.compile(s)
    except:
        return False
    return True
------------------------------------------------------------------------------------
"""
