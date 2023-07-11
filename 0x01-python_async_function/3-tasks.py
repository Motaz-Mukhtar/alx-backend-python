#!/usr/bin/env python3
"""
    Write regular function def task_wait_random()
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
        Take an integer max_delay and returns a asycio.Task.
    """
    new_task = asyncio.create_task(wait_random(max_delay))
    return new_task
