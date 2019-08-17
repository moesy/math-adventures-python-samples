"""
Book: Math Adventures with Python
Chapter: Introduction

Implement "The Problem with School Math" section
"""
from typing import Union
import math


def f(x: float) -> float:
    """
    :param x: an input.
    :return: the value of the expression f(x)
    """
    return math.sqrt(x+3) - x + 1


def g(t: float) -> Union[int, float]:
    """
    :param t: an  input.
    :return: the value of the expression g(t)
    """
    return t**2 - 1


def h(x: float) -> Union[int, float, None]:
    """
    :param x: an  input.
    :return: the value of the expression h(x)
    """
    try:
        return x**2 + (1/x) + 2

    except ZeroDivisionError:
        return None


if __name__ == '__main__':
    # TODO: Accept safe inputs from cli and remove hard coded values
    inputs = [0, 1, math.sqrt(2), math.sqrt(2)-1]

    for y in inputs:
        print("f({:.3f}) = {:.3f}".format(y, f(y)))
        print("g({:.3f}) = {:.3f}".format(y, g(y)))
        print("h({:.3f}) = {}".format(y, h(y)))
