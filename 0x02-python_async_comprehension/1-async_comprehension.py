#!/usr/bin/env python3
"""
    Write a coroutine async def async_comprehension()
"""
from typing import List


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
        The coroutine will collect 10 random numbers
        using an async comprehensing over async_generator,
        then return the 10 random numbers.
    """
    random_numbers_list = []

    async for rand_num in async_generator():
        random_numbers_list.append(rand_num)
    return random_numbers_list