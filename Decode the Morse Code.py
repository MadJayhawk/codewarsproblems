# 6 kyu  Python
# https://www.codewars.com/kata/decode-the-morse-code/train/python
import pytest
def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))

if __name__ == '__main__':
    print(decodeMorse())

