#!/usr/bin/python3
"""
Making a Pascal Triangel
"""


def pascal_triangle(n):
    """
	pascal_triangle(n) that generates and returns a list of lists representing the first n rows of Pascal's triangle
    """
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            res.append(level)
    return res
