# 5 kyu  Python
# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
def make_readable(seconds):
    hr = str(seconds // 3600).zfill(2)
    minute = str((seconds % 3600) // 60).zfill(2)
    sec = str((seconds % 3600) % 60).zfill(2)
    return "{}:{}:{}".format(hr, minute, sec)


if __name__ == "__main__":
    s = 0
    print(make_readable(s))

"""
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
"""
