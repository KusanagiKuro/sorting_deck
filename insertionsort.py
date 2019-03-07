#!/usr/bin/env python3
from utility import *


def insertionSort(lst, gui=False):
    """
    Insertion Sort Algorithm
    """
    for index in range(1, len(lst)):
        key = lst[index]
        count = index - 1
        check = False
        while count >= 0 and key < lst[count]:
            lst[count + 1] = lst[count]
            count -= 1
            check = True
        lst[count + 1] = key
        if check:
            print(*lst)
    return True
