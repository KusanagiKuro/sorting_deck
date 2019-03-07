#!/usr/bin/env python3
from utility import *


def mergeSort(lst, gui=False):
    """
    Merge Sort Algorithm
    """
    if len(lst) > 1:
        # Break the list into 2 halves and apply merge sort on them
        mid = len(lst) // 2
        leftHalf = lst[:mid]
        rightHalf = lst[mid:]
        mergeSort(leftHalf)
        mergeSort(rightHalf)
        i = j = k = 0
        # After the merge sort of the two halves, merge them
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                lst[k] = leftHalf[i]
                i += 1
            else:
                lst[k] = rightHalf[j]
                j += 1
            k += 1
        while i < len(leftHalf):
            lst[k] = leftHalf[i]
            i += 1
            k += 1
        while j < len(rightHalf):
            lst[k] = rightHalf[j]
            j += 1
            k += 1
        print(*lst)
    return True
