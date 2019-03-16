#!/usr/bin/env python3
from command import *


def mergeSort(lst, commandList):
    """
    Merge Sort Algorithm (Out of Place)

    Input: @lst: List of integers that we need to sort.
           @commandList: List. The list of commands that the GUI will run on
    """
    if len(lst) > 1:
        # Break the list into 2 halves and apply merge sort on them
        mid = len(lst) // 2
        leftHalf, rightHalf = lst[:mid], lst[mid:]
        mergeSort(leftHalf, commandList)
        mergeSort(rightHalf, commandList)

        # After the merge sort of the two halves, merge them
        mergeOutOfPlace(lst, leftHalf, rightHalf, commandList)
    return True


def mergeOutOfPlace(lst, leftHalf, rightHalf, commandList):
    """
    Merging the two halves of the list using out of place method.

    Input: @lst: List of integers that we need to sort.
           @leftHalf: List. The left half of the list.
           @rightHalf: List. The right half of the list.
           @commandList: List. The list of commands that the GUI will run on
    """
    # Compare and add the elements between two halves back to the list till
    # one of them is empty
    left, right, mergeSlot = addInOrder(lst, leftHalf, rightHalf, commandList)

    # Add the remaining of the other half to the list.
    if right >= len(rightHalf):
        addRemaining(lst, left, leftHalf, mergeSlot, commandList)
    elif left >= len(leftHalf):
        addRemaining(lst, right, rightHalf, mergeSlot, commandList)
    print(*lst)


def addInOrder(lst, leftHalf, rightHalf, commandList):
    """
    Comparing the elements between two halves and add them back to the list
    until one of halves is empty.

    Input: @lst: List of integers that we need to sort.
           @leftHalf: List. The left half of the list.
           @rightHalf: List. The right half of the list.
           @commandList: List. The list of commands that the GUI will run on

    Output: left: The position of the left marker after this step.
            right: The position of the right marker after this step.
            mergeSlot: The current index that needs to be added in the list.
    """
    # Setup the left, right marker, as well as the current slot in the list.
    left = right = mergeSlot = 0

    # Compare and add the element from the two halves back to the list when
    # they meet the condition
    while left < len(leftHalf) and right < len(rightHalf):
        if leftHalf[left] < rightHalf[right]:
            lst[mergeSlot] = leftHalf[left]
            left += 1
        else:
            lst[mergeSlot] = rightHalf[right]
            right += 1
        mergeSlot += 1
    return left, right, mergeSlot


def addRemaining(lst, marker, half, mergeSlot, commandList):
    """
    Add all the remaining of the half to the list

    Input: @lst: List of integers that we need to sort.
           @marker: integer. The current position of the marker of that part.
           @half: integer. The current half that still has elements in it.
           @mergeSlot: integer. The current index of the slot in the list.
           @commandList: List. The list of commands that the GUI will run on
    """
    while marker < len(half):
        lst[mergeSlot] = half[marker]
        marker += 1
        mergeSlot += 1
