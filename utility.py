#!/usr/bin/env python3
import pyglet
from pyglet import *


def swap(lst, first, second):
    """
    Swap value between two elements of a lst if the first is higher
    """
    lst[first], lst[second] = lst[second], lst[first]
    return True
