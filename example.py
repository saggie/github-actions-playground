# example.py - A sample file to be formatted by Black

import os
import sys


# Blackはダブルクォートを推奨するため、この行は変更される
def my_function(a, b, c, d, e, f, g, h, i, j, k, l, m, n):
    """This is a docstring that uses single quotes."""

    # 長すぎる行はBlackによって改行される
    result = a + b + c + d + e + f + g + h + i + j + k + l + m + n

    print ("The result is:", result)

    # 辞書のインデントもフォーマットされる
    my_dict = {"key1": "value1", "key2": "value2"}

    return result, my_dict


if __name__ == "__main__":
    # 引数のインデントもフォーマットされる
    my_function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
