# 5 kyu  Python
# https://www.codewars.com/kata/5e07b5c55654a900230f0229/train/python


def reverse_in_parentheses(s):
    stack = []
    for i in s:
        stack.append(i)
        if i == ")":
            opening = len(stack) - stack[::-1].index("(") - 1
            stack.append(
                "".join(
                    [
                        i[::-1].translate(str.maketrans("()", ")("))
                        for i in stack[opening:][::-1]
                    ]
                )
            )
            del stack[opening:-1]

    return "".join(stack)


if __name__ == "__main__":
    x = "h(el)lo"
    print(reverse_in_parentheses(x))
    """
    --------------------------------------------------------------------
    
    def reverse_in_parentheses(string):
    a = 0
    for n in range(string.count("(")):
        a, b = string.find("(", a), 0
        for i in range(a, len(string)):
            if string[i] == "(": 
                b += 1
            elif string[i] == ")": 
                b -= 1
            if b == 0: break
        a += 1
        string = string[:a] + string[a:i][::-1].translate(str.maketrans(")(", "()")) + string[i:]
    return string
"""
