#!/usr/bin/env python3
"""
    Write Coroutine def wait_n()
"""
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        Will spawn wait_random, n times with the
        specified max_delay, should return the list
        of all the delays (float, values), the list
        should be in ascending order.
    """
    random_numbers: List[float] = []

    for i in range(n):
        random_numbers.append(await wait_random(max_delay))

    return sorted(random_numbers)
