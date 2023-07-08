#!/usr/bin/env python3
"""
    Write function to_kv that takes a string k
    and an int OR float v as arguments and returns
    a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Takes a string k and an int OR float v
        returns Tuple, The first element of the tuple
        is the string k, The second element is the square
        of the int/float and should be annotated as a
        float.
    """
    return (k, v**2)
