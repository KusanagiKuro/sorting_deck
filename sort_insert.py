#!/usr/bin/env python3
from command import addCommand
from utility import compareValueInList


def insert(lst, index, commandList):
    """
    Loop through the list to find insert point

    Input: @lst: List of integers that we need to sort.
           @index: integer. Current index.
           @commandList: List. The list of commands that the GUI will run on

    Output: True if the insertion happened. False if it didn't.
    """
    # Set the key equal to the value of the current index
    key = lst[index]

    # Setup default return value
    check = False

    # Loop backward from the previous index to the start of the list
    for index2 in range(index - 1, -2, -1):
        if index2 < 0:
            break

        # If the value of the index is less than the value of the key
        if compareValueInList(lst, commandList, index, index2,
                              key, lst[index2], "Key < lst[index]?"):

            # Shift the value of the index to the right
            lst[index2 + 1] = lst[index2]
            check = True
            addCommand(commandList, "UpdateStatus", [index, index2],
                       "normal")

        # Else end the loop
        else:
            addCommand(commandList, "UpdateStatus", [index, index2],
                       "normal")
            break
    # Set the key to its correct position
    if check:
        addCommand(commandList, "Shift", index, index2 + 1)
        lst[index2 + 1] = key
    else:
        addCommand(commandList, "UpdateStatus", [index], "normal")
    return check


def insertionSort(lst, commandList):
    """
    Insertion Sort Algorithm

    Input: @lst: List of integers that we need to sort.
           @commandList: List. The list of commands that the GUI will run on
    """
    # Loop through the list from index 1 to the end
    for index in range(1, len(lst)):

        # Find the insert point for the element in that index
        # Print the list if needed
        if insert(lst, index, commandList):
            print(*lst)
