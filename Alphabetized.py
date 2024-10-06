# 6 kyu  Python
# https://www.codewars.com/kata/alphabetized/train/python


    c=0
    d=[]
    b=[]
    for i in s:
        c+=1
        if i not in "'`!@#$%^&*()_-+=<>,." and i !=' ':
            d.append([i.lower(),c,i])
    for i in sorted(d):
        b.append(i[2])
        
    return ''.join(b)

if __name__ == '__main__':
    t="CodeWars can't Load Today"
    alphabetized(t)
