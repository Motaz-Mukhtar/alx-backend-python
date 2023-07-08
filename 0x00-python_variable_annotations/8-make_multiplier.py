#!/usr/bin/env python3
"""
    Write function make_multiplier() that
    takes a float multiplier and returns
    a function that multiplies a float
    by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Takes a float multiplier and returns a function
        that multplies a float by multiplier.
    """
    def multiplier(mul: float) -> float:
        """
            returns multiplies float of mul
        """
        return mul**2
    return multiplier
