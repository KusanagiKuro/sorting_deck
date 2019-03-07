#!/usr/bin/env python3
from utility import *


def quickSortCall(lst, gui):
    """
    Call for quick sort algorithm
    """
    quickSort(lst, 0, len(lst) - 1)
    return True


def quickSort(lst, start, end):
    """
    Quick Sort Algorithm
    """
    if start < end:
        # Set left counter to start, right counter to end and the pivot
        # is the first element
        # Left counter indicates the split point for the part that is less than
        # pivot, same for right counter but for the part that is greater than
        # pivot
        left, right, pivot = start, end, lst[start]
        # Stop when the left counter is higher than the right counter
        while left <= right:
            # If left value > pivot > right value
            # Swap the left and right value
            if lst[left] > pivot > lst[right]:
                swap(lst, left, right)

            # Raise left counter if left value <= pivot
            if lst[left] <= pivot:
                left += 1

            # Lower right counter if left value > pivot, right value >= pivot
            elif lst[left] > pivot and lst[right] >= pivot:
                right -= 1

        # Swap the pivot to its right location (which is indicated by the left
        # counter)
        swap(lst, start, left - 1)
        print('P:', pivot)
        print(*lst)
        # Apply quick sort for the two parts
        quickSort(lst, start, left - 2)
        quickSort(lst, left, end)
    return True
