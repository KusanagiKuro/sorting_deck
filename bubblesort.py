#!/usr/bin/env python3
import os
from utility import *


def bubbleSort(lst, gui=False):
    """
    Bubble Sort Algorithm
    """
    size = len(lst)
    for firstCounter in range(size):
        for secondCounter in range(size - firstCounter - 1):
            if gui:
                gui.write("Compare", secondCounter, secondCounter + 1)
            if lst[secondCounter] > lst[secondCounter + 1]:
                if gui:
                    gui.write("Result", secondCounter, secondCounter + 1,
                              "greater")
                swap(lst, secondCounter, secondCounter + 1)
                print(*lst)
            elif gui:
                result = ("less" if lst[secondCounter] < lst[secondCounter + 1]
                          else "equal")
                gui.write("Result", secondCounter, secondCounter + 1,
                          result)
    return True
