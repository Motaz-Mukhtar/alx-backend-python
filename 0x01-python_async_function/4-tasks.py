#!/usr/bin/env python3
"""
    Write regular fucntion def task_wait_n()
"""
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        Will spawn wait_random, n times with the
        specified max_delay, should return the list
        of all the delays (float, values), thelist
        should be in ascending order
    """
    random_numbers: List[float] = []

    for i in range(n):
        random_numbers.append(await task_wait_random(max_delay))

    return sorted(random_numbers)
