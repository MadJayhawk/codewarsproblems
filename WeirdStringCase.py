# 6 kyu  Python
# https://www.codewars.com/kata/52b757663a95b11b3d00062d/train/python


def to_weird_case(string):
    h = string.split()
    d = []
    e = []
    for word in h:
        for i, j in enumerate(word, 0):
            if i % 2 == 0:
                d.append(j.upper())
            else:
                d.append(j.lower())
        e.append("".join(d))
        d = []
    return " ".join(e)


if __name__ == "__main__":
    # x = ["String", "Weird string case", "This", "is", "This is a test"]
    # for i in x:
    i = "Weird string case"
    print(to_weird_case(i))

"""
-----------------------------------------------------------------------------------------
def to_weird_case(string):
    recase = lambda s: "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])
    return " ".join([recase(word) for word in string.split(" ")])

------------------------------------------------------------------------------------------
def to_weird_case(string):
    return ' '.join([''.join([y.lower() if i%2 else y.upper() for i, y in enumerate(x)]) for x in string.split()])
    
  https://stackoverflow.com/questions/13668829/replace-every-nth-letter-in-a-string  
------------------------------------------------------------------------------------------
"""
