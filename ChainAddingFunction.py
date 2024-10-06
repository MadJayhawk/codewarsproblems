# 5 kyu  Python
# https://www.codewars.com/kata/539a0e4d85e3425cb0000a88/train/python

#  https://stackoverflow.com/questions/39038358/function-chaining-in-python#comment65432772_39039586


class CustomInt(int):
    def __call__(self, v):
        return CustomInt(self + v)


def add(v):
    return CustomInt(v)


if __name__ == "__main__":
    x = 1
    print(add(x))
