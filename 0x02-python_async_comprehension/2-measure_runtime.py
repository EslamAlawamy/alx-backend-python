#!/usr/bin/env python3
""" 2-measure_runtime.py Module """


import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """ measure_runtime function """
    start: float = time.perf_counter()

    tasks = [async_comprehension() for i in range(4)]

    await asyncio.gather(*tasks)

    end: float = time.perf_counter()

    return end - start
