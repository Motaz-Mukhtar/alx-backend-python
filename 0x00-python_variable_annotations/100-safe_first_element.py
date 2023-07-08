#!/usr/bin/env python3
"""
    Code with the correct duc-typed
    annotations.
"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        Return the first Element at lst list or None
    """
    if lst:
        return lst[0]
    else:
        return None
