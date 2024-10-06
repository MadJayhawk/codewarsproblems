# 5 kyu  Python
# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python


def first_non_repeating_letter(a):

    if len(a) == 1:
        return a
    if len(a) == 0:
        return ""
    b = a.lower()
    for i in b:
        if b.count(i.lower()) == 1:
            return a[b.index(i)]

    return ""


if __name__ == "__main__":
    x = "a"
    print(first_non_repeating_letter(x))
# ---------------------------------------------------------------------------

# def first_non_repeating_letter(string):
#     string_lower = string.lower()
#     for i, letter in enumerate(string_lower):
#         if string_lower.count(letter) == 1:
#             return string[i]
#
#     return ""
