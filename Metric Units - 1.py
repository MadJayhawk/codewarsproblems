# 5 kyu  Python
# https://www.codewars.com/kata/metric-units-1/train/python

m = {'Y': 1000000000000000000000000, 'Z': 1000000000000000000000, 'E': 1000000000000000000, 'P': 1000000000000000,
	 'T': 1000000000000, 'G': 1000000000, 'M': 1000000, 'k': 1000, 'h': 100, 'da': 10, 'm': 1}
def meters(x):
    v = 0
    j = ''
    w={k: v for k, v in sorted(m.items(), key=lambda item: item[1])}
    for i, j in w.items():
        if x >= j:
            if i=='m':
                i=''
            u=x/j
            if int(u) == float(u):
                u = int(u)
            else:
                u = float(u)
            v = str(u) + i + 'm'
    return v


if __name__ == '__main__':
    print(meters(999))



