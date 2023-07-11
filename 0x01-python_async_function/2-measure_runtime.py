#!/usr/bin/env python3
"""
    Create def measure_time()
"""
import time
import asyncio


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        Measures the totla execution time
        for wait_n(n, amx_delay), and returns
        totla_time / n.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    end = end - start
    return end / n
