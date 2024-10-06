# 5 kyu  Python
# https://www.codewars.com/kata/59de1e2fe50813a046000124/train/python

import re


def change(s, prog, version):
    regex_phone = "[+]\d-\d{3}-\d{3}-\d{4}"
    regex_version = "\d+[.]\d+"
    regex_version_2_0 = "([2]+\.[0])"
    if re.findall(regex_phone, s) == []:
        return "ERROR: VERSION or PHONE"
    if re.findall(regex_version_2_0, s) != []:
        version = "2.0"
    else:
        if re.findall(regex_version, version)[0] != version:
            return "ERROR: VERSION or PHONE"
    return (
        "Program: "
        + prog
        + " Author: g964"
        + " Phone: "
        + "+1-503-555-0090"
        + " Date: 2019-01-01"
        + " Version: "
        + version
    )


if __name__ == "__main__":
    s1 = (
        "Program title: Primes\nAuthor: Kern\nCorporation: Gold\nPhone: +1-503-555-0911\nDate: Tues April 9, "
        "2005\nVersion: 6.7\nLevel: Alpha"
    )
    s11 = (
        "Program title: Hammer\nAuthor: Tolkien\nCorporation: IB\nPhone: +1-503-555-0290\nDate: Tues March 29, "
        "2017\nVersion: 2.0\nLevel: Release"
    )
    s12 = (
        "Program title: Primes\nAuthor: Kern\nCorporation: Gold\nPhone: +1-503-555-556\nDate: Tues April 9, "
        "2005\nVersion: 5.5\nLevel: Alpha"
    )
    print(change(s1, "Ladder", "1.1"))
    print(change(s11, "Balance", "1.5.6"))
    print(change(s12, "Ladder", "1.1"))
#
# "Program: Balance Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: 2.0"
# "Program: Balance Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: 1.5.6"
