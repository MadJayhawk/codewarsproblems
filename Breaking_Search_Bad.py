# 6 kyu  Python
# https://www.codewars.com/kata/52cd53948d673a6e66000576/train/python
import pytest


def search(titles, term):
    d = []
    for i in titles:
        if term in i.lower():
            d.append(i)
    return d


if __name__ == "__main__":
    titles = [
        "The Big Bang Theory",
        "How I Met Your Mother",
        "Dexter",
        "Breaking Bad",
        "Doctor Who",
        "The Hobbit",
        "Pacific Rim",
        "Pulp Fiction",
        "The Avengers",
        "Shining",
    ]
    s = ["the"]

    for i in s:
        print(search(titles, i))
        print()
    # ------------------------------------------------------------------------
    # def search(titles, term):
    #     return list(filter(lambda title: term in title.lower(), titles))
