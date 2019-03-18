#!/usr/bin/env python3
from command import addCommand
from utility import compareValueInList


def mergeSortInPlaceCall(lst, commandList):
    """
    Call the in place merge sort

    Input: @lst: List of integers that we need to sort.
           @commandList: List. The list of commands that the GUI will run on
    """
    mergeSortInPlace(lst, 0, len(lst), commandList)


def mergeSortInPlace(lst, start, end, commandList):
    """
    In-place Merge Sort

    Input: @lst: list. The list we need to sort.
           @start: integer. The starting index of the part.
           @end: integer. The ending index of the part.
           @commandList: List. The list of commands that the GUI will run on
    """
    if start < end - 1:
        # Define the split point
        mid = start + (end - start) // 2
        addCommand(commandList, "Split", start, mid, end)

        # Using merge sort on the two halves.
        mergeSortInPlace(lst, start, mid, commandList)
        mergeSortInPlace(lst, mid, end, commandList)

        # After that, merge them
        mergeInPlace(lst, start, end, mid, commandList)
        print(*lst[start:end])


def mergeInPlace(lst, start, end, mid, commandList):
    """
    Merge the two parts of the list.

    Input: @lst: list. The list we need to sort.
           @start: integer. The starting index of the part.
           @end: integer. The next index after the end of the part
           @mid: integer. The split point between the two parts.
           @commandList: List. The list of commands that the GUI will run on.
    """
    # Return if this part of the list only has 1 element.
    if start >= end - 1:
        return

    addCommand(commandList, "UpdateStatus",
               [index for index in range(len(lst))
                if index < start or index >= end],
               "locked")

    # Mark the starting index of the second part. It will start at the split
    # point.
    start2 = mid
    if compareValueInList(lst, commandList, start2 - 1, start2,
                          lst[start2 - 1], lst[start2],
                          "lst[mid - 1] <= lst[mid]?"):
        addCommand(commandList, "UpdateStatus",
                   [index for index in range(len(lst))
                    if index < start or index >= end - 1],
                   "normal")
        return
    addCommand(commandList, "UpdateStatus", [start2, start2 - 1], "normal")
    # Start rearranging the elements between the two parts until one of them
    # meet their end.
    while start < mid and start2 < end:
        start, start2, mid = rearrangeInPlace(lst, start, start2,
                                              mid, commandList)
    addCommand(commandList, "UpdateStatus",
               [index for index in range(len(lst))
                if index < start or index >= end - 1],
               "normal")


def rearrangeInPlace(lst, start, start2, mid, commandList):
    """
    Rearrange the two elements inside different parts of the list

    Input: @start: integer. The marker for current index of the first part.
                   Which is the index of the 1st element
           @start2: integer. The marker for current index of the second part.
                    Which is the index of the 2nd element.
           @mid: integer. The split point of the two parts that these 2
                 elements are in.
           @commandList: List. The list of commands that the GUI will run on.

    Ouput: @start: The next index that needs to be checked for the first part
           @start2: The next index that needs to be checked for the second part
           @mid: The new split point of the two parts
    """
    # Compare the two elements, if the 1st one is greater, move to the next
    # element of the 1st part.
    if compareValueInList(lst, commandList, start, start2, lst[start],
                          lst[start2], "lst[left] <= lst[right]?"):
        addCommand(commandList, "UpdateStatus", [start, start2],
                   "normal")
        start += 1

    # Else
    else:
        # Store the current index and value of the 2nd element
        value, index = lst[start2], start2
        addCommand(commandList, "UpdateStatus", [start],
                   "normal")
        addCommand(commandList, "Shift", start2, start)

        # Shift all elements between the 1st and the 2nd to the right.
        # (Including the 1st, but not the 2nd)
        while index > start:
            lst[index] = lst[index - 1]
            index -= 1

        # Set the index and value of the current 1st element to the stored
        # index and value
        lst[start] = value

        # Move the marker to the next element, as well as push the split point
        # between two halves to the right by 1.
        start += 1
        mid += 1
        start2 += 1
    return start, start2, mid
