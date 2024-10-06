# 6 kyu  Python
# https://www.codewars.com/kata/55f4a44eb72a0fa91600001e/train/python


class CustomInt(str):
    def __call__(self, v=""):
        if v == "":
            return CustomInt(self + v).strip()
        return CustomInt(self + v + " ")


def create_message(v):
    return CustomInt(v + " ")


if __name__ == "__main__":
    print(create_message("Hello")("World!")("how")("are")("you?")())
