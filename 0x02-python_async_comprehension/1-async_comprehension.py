#!/usr/bin/env python3
"""Import async_generator  write a coroutine
called async_comprehensionen that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing
over async_generator, then return the 10 random numbers.
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return the 10 random numbers"""
    results = [i async for i in async_generator()]
    return results
