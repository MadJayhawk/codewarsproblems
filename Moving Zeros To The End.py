# 5 kyu  Python
# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python


def move_zeros(array):
    d = []
    e = []
    for s in array:
        if type(s) == bool:
            d.append(s)
        else:
            if s == 0:
                e.append(0)
            else:
                d.append(s)
    return d + e


if __name__ == "__main__":
    x = [False, 1, 0, 1, 2, 0, 1, 3, "a"]
    print(move_zeros(x))

"""
def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)

-----------------------------------------------------------
def move_zeros(array):
    newarr =[]
    zeroarr=[]
    for item in array:
        if item!= 0 or type(item)== bool :
            newarr.append(item)
        else:
            zeroarr.append(item)


    newarr.extend(zeroarr)
    return(newarr)
    --------------------------------------------
    def move_zeros(arr):
        a = [i for i in arr if isinstance(i, bool) or i!=0]
        return a+[0]*(len(arr)-len(a))

"""
