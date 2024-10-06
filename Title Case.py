# 6 kyu  Python
# https://www.codewars.com/kata/5202ef17a402dd033c000009/train/python

import string


def title_case(title, f=""):
    if title == "":
        return ""
    a = title.lower().split()
    b = f.lower().split()
    d = []
    d.append(a[0].capitalize())
    for i in a[1:]:
        if i in b:
            d.append(i)
        else:
            d.append(i.capitalize())
    return " ".join(d)


if __name__ == "__main__":
    print(title_case("THE WIND IN THE WILLOWS", "The In"))
