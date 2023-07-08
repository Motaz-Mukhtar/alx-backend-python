#!/usr/bin/env python3
"""
    Write function sum_mixed_list() that takes
    a list mxd_lst of integers and floats and
    returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        Takes a list mxd_lst of integers
        and floats and returns their sum
        as a float.
    """
    mixed_sum: int = 0

    for mix in mxd_lst:
        mixed_sum += mix

    return mixed_sum
