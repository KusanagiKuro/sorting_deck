#!/usr/bin/env python3
from command import *
from utility import swapValueInList


def quickSortCall(lst, commandList):
    """
    Call for quick sort algorithm
    """
    return quickSort(lst, 0, len(lst) - 1, commandList)


def quickSort(lst, start, end, commandList):
    """
    Quick Sort Algorithm

    Input: @lst: List of integers that we need to sort.
           @commandList: List. The list of commands that the GUI will run on
    """
    if start < end:
        # Search for the split point of the list
        makeCommand(commandList, "UpdateStatus",
                    [index for index in range(len(lst))], "locked")
        makeCommand(commandList, "UpdateStatus",
                    [index for index in range(start, end + 1)], "normal")
        left, right, pivot = searchForPartition(lst, start, end, commandList)
        print('P:', pivot)
        print(*lst)
        # Apply quick sort for the two partition
        makeCommand(commandList, "Split", start, left, end + 1)
        quickSort(lst, start, left - 2, commandList)
        quickSort(lst, left, end, commandList)


def searchForPartition(lst, start, end, commandList):
    """
    Search for the partition

    Input: @lst: List of integers that we need to sort.
           @start: integer. The starting index of the current part of the list
           @end: integer. The ending index of the current part of the list
           @commandList: List. The list of commands that the GUI will run on
    """
    # Setup 2 markers, at the start and at the end
    makeCommand(commandList, "CreateMarkers", start, end, start)
    left, right, pivot = start, end, lst[start]

    # Stop when the left marker is higher than the right marker
    while left <= right:
        # If left value > pivot > right value
        # Swap left value and right value
        if lst[left] > pivot > lst[right]:
            makeCommand(commandList, "Swap", left, right)
            swapValueInList(lst, left, right)

        # Raise left marker if left value <= pivot
        if lst[left] <= pivot:
            left += 1
            makeCommand(commandList, "MoveLeftMarker", 0, left)

        # Lower right marker if left value > pivot and right value >= pivot
        elif lst[left] > pivot and lst[right] >= pivot:
            right -= 1
            makeCommand(commandList, "MoveRightMarker", 1, right)

    # Swap the pivot to its right location (which is indicated by the left
    # marker)
    makeCommand(commandList, "Swap", start, left - 1)
    swapValueInList(lst, start, left - 1)
    return left, right, pivot
