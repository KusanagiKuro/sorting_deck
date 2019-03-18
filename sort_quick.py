#!/usr/bin/env python3
from command import addCommand
from utility import swapValueInList, compareValueInList


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
        addCommand(commandList, "UpdateStatus",
                   [index for index in range(len(lst))], "locked")
        addCommand(commandList, "UpdateStatus",
                   [index for index in range(start, end + 1)], "normal")
        left, right, pivot = searchForPartition(lst, start, end, commandList)
        print('P:', pivot)
        print(*lst)
        # Apply quick sort for the two partition
        addCommand(commandList, "Split", start, left, end + 1)
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
    addCommand(commandList, "HideMarkers")
    addCommand(commandList, "CreateMarkers", start + 1, end, start)
    left, right, pivot = start + 1, end, lst[start]

    # Stop when the left marker is higher than the right marker
    while left <= right:
        # If left value > pivot > right value
        # Swap left value and right value
        if (compareValueInList(lst, commandList, left, start, lst[left], pivot,
                               "lst[left] > pivot?")
                and
                compareValueInList(lst, commandList, start, right, pivot,
                                   lst[right], "pivot > lst[right]?")):
            swapValueInList(lst, left, right, commandList)
        addCommand(commandList, "UpdateStatus", [left, start, right], "normal")
        # Raise left marker if left value <= pivot
        if compareValueInList(lst, commandList, left, start, lst[left],
                              pivot, "lst[left] <= pivot?"):
            addCommand(commandList, "UpdateStatus", [left], "normal")
            left += 1
            addCommand(commandList, "MoveLeftMarker", 0, left)

        # Lower right marker if left value > pivot and right value >= pivot
        elif compareValueInList(lst, commandList, right, start, lst[right],
                                pivot, "lst[right] >= pivot?"):
            addCommand(commandList, "UpdateStatus", [left], "normal")
            addCommand(commandList, "UpdateStatus", [right], "normal")
            right -= 1
            addCommand(commandList, "MoveRightMarker", 1, right)
        else:
            addCommand(commandList, "UpdateStatus", [left], "normal")
            addCommand(commandList, "UpdateStatus", [right], "normal")

    # Swap the pivot to its right location (which is indicated by the left
    # marker)
    swapValueInList(lst, start, left - 1, commandList)
    return left, right, pivot
