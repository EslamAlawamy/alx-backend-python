#!/usr/bin/env python3
""" 4-tasks.py module """
import asyncio
from typing import List


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_n
    @n: times to call wait_random.
    @max_delay: max delay of wait_random.
    Return: the list of all delays.
    """
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
