#!/usr/bin/env python3
from command import addCommand
from utility import swapValueInList, compareValueInList


def compareInPair(lst, index, commandList):
    """
    Compare each element in list with its right neighbor and swap if needed.

    Input: @lst: List of integers. The list we need to sort.
           @index: Integer. The starting index.
           @commandList: List. The list of commands that the GUI will run on
    """
    # Setup a check variable that indicates if a swap happens.
    check = False

    # Loop through each element in a certain range.
    for index2 in range(len(lst) - index - 1):
        # Compare that element with the element next to it.
        if compareValueInList(lst, commandList, index2, index2 + 1,
                              lst[index2], lst[index2 + 1],
                              "lst[n] > lst[n+1]?"):
            # If it's greater, swap them.
            swapValueInList(lst, index2, index2 + 1, commandList)

            # Set the check variable to True
            check = True

            # Print out the list
            print(*lst)
        addCommand(commandList, "UpdateStatus", [index2, index2 + 1],
                   "normal")
    addCommand(commandList, "UpdateStatus", [len(lst) - 1 - index], "locked")
    return check


def bubbleSort(lst, commandList):
    """
    Bubble Sort Algorithm

    Input: @lst: List of integers that we need to sort.
           @commandList: List. The list of commands that the GUI will run on
    """
    # Run through the list n time
    for index in range(len(lst)):

        # For each loop, check each pair of elements and swap if needed
        # If no swap happened, the list is already sorted so we can stop.
        if not compareInPair(lst, index, commandList):
            break
