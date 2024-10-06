# 6 kyu  Python
# https://www.codewars.com/kata/5d23d89906f92a00267bb83d/train/python


def get_order(order):
    menu = "Burger Fries Chicken Pizza Sandwich Onionrings Milkshake Coke".split()
    d = []
    neworder = order
    for i in range(len(menu)):
        try:
            while neworder.index(menu[i].lower()) >= 0:
                a = neworder.index(menu[i].lower())
                b = a + len(menu[i])
                neworder = neworder[0:a] + neworder[b:]
                d.append(menu[i])
        except ValueError:
            pass
    return " ".join(d)


"""
MENU = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"]

def get_order(order):
    result = []
    for item in MENU:
        result.extend([item for _ in range(order.count(item.lower()))])
    return " ".join(result)
 ---------------------------------------------------------------------   
 def get_order(order):
    menu = ['burger', 'fries', 'chicken', 'pizza', 'sandwich', 'onionrings', 'milkshake', 'coke']
    clean_order = ''
    for i in menu:
        clean_order += (i.capitalize() + ' ') * order.count(i)
    return clean_order[:-1]
 ----------------------------------------------------------------------   
import re

MENU = ['burger', 'fries', 'chicken', 'pizza', 'sandwich', 'onionrings', 'milkshake', 'coke']

def get_order(order):
    res = []
    for item in MENU:
        res.extend(re.findall(item, order))
    return ' '.join([item.capitalize() for item in res])   


"""


if __name__ == "__main__":
    a = "pizzachickenfriesburgercokemilkshakefriessandwich"

    print(get_order(a))
