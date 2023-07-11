#!/usr/bin/env python3
"""
    Write a coroutine async def async_generator()
"""
from typing import Iterator
import random
import asyncio


async def async_generator() -> Iterator[float]:
    """
        The coroutine will loop 10 times
        asynchroously wait 1 second, then
        yield a random number betwee 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
