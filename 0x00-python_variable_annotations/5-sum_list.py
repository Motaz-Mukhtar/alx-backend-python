#!/usr/bin/env python3
"""
    Write function sum_list() that takes
    a list input_list of floats and returns
    thier sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        Take input_list of floats and returns
        their sum as a float.
    """
    float_sum: int = 0

    for num in input_list:
        float_sum += num

    return float_sum
