''' 
6 kyu  Python
https://www.codewars.com/kata/59e19a747905df23cb000024/train/python

'''
def string_letter_count(s):
    d = []
    k=s.lower()
    b = 'abcdefghijklmtnopqrstuvwxyz'
    for i in b:
        c = s.count(i)
        if c > 0:
            t = str(c) + i
            d.append(t)
        else:
            pass

    return "".join(d)

if __name__ == '__main__':
    ss = "c at"
    print(string_letter_count(ss))
# -----------------------------------------------------------------
# def string_letter_count(s):
#     s = s.lower()
#     m = ''
#     for i in sorted(list(set(s))):
#         if i.islower():
#             m += str(s.count(i)) + i
#     return m
