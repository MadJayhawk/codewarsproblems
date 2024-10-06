# 6 kyu  Python
# https://www.codewars.com/kata/54b724efac3d5402db00065e/discuss


def validSolution(s):
    sp = [[0, 0], [3, 0], [6, 0], [0, 3], [3, 3], [6, 3], [0, 6], [3, 6], [6, 6]]

    # Checking row validity of every row
    for r in range(9):
        d = set()
        for c in range(9):
            print(r, c, s[r][c])
            if s[r][c] == 0:
                d.add(s[r][c])
            else:
                if s[r][c] in d:
                    return False
            d.add(s[r][c])
    # Checking row validity of every column
    for c in range(9):
        d = set()
        for r in range(9):
            print(r, c, s[r][c])
            if s[r][c] == 0:
                d.add(s[r][c])
            else:
                if s[r][c] in d:
                    return False
            d.add(s[r][c])
    for a, b in sp:
        d = set()
        for r in range(3):
            for c in range(3):
                print(r, c, s[c + b][r + a])
                if s[c + b][r + a] in d:
                    return False
                else:
                    d.add(s[c + b][r + a])
    return True
if __name__ == '__main__':

    print(validSolution(s))


    

