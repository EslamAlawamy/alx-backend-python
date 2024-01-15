#!/usr/bin/env python3
""" 8-make_multiplier.py"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ a function that multiplies a float by multiplier """

    return lambda x: x * multiplier
