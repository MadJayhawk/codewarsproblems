# 6 kyu
#  https://www.codewars.com/kata/help-the-bookseller/train/python

def stock_list(listOfArt, listOfCat):
    if not listOfArt:
        return ''
    cat = {}
    for i in listOfCat:
        cat[i[0]] = 0
    d = []
    for i in listOfArt:
        if i[0] in cat:
            cat[i[0]] += int("".join(filter(str.isdigit, i)))

    for i, j in cat.items():
        d.append("(" + i + " : " + str(j) + ")")
    return " - ".join(d)


if __name__ == '__main__':
    L= ['ABAR 200', 'CDXE 500', 'BKWR 250', 'BTSQ 890', 'DRTY 600']
    M=['A', 'B']
    # L = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
    # M = ["A", "B", "C", "D"]

    ['ROXANNE 102', 'RHODODE 123', 'BKWRKAA 125', 'BTSQZFG 239', 'DRTYMKH 060']
    ['B', 'R', 'D', 'X']
    '(B : 364) - (R : 225) - (D : 60) - (X : 0)'

    []
    ['B', 'R', 'D', 'X']
    ''

    ['ROXANNE 102', 'RHODODE 123', 'BKWRKAA 125', 'BTSQZFG 239', 'DRTYMKH 060']
    ['U', 'V', 'R']
    '(U : 0) - (V : 0) - (R : 225)'