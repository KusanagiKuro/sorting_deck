#!/usr/bin/env python3
import os
from utility import swap, makeCommand


def bubbleSort(lst, commandList):
    """
    Bubble Sort Algorithm
    """
    size = len(lst)
    commandList = [makeCommand("CreateList", lst)]
    for firstCounter in range(size):
        for secondCounter in range(size - firstCounter - 1):
            commandList.append(makeCommand("Compare", secondCounter,
                                           secondCounter + 1))
            if lst[secondCounter] > lst[secondCounter + 1]:
                commandList.append(makeCommand("Result", secondCounter,
                                               secondCounter + 1,
                                               "greater"))
                commandList.append(makeCommand("Swap", secondCounter,
                                               secondCounter + 1))
                swap(lst, secondCounter, secondCounter + 1)
                print(*lst)
            else:
                result = ("less" if lst[secondCounter] < lst[secondCounter + 1]
                          else "equal")
                commandList.append(makeCommand("Result", secondCounter,
                                               secondCounter + 1,
                                               result))
        commandList.append(makeCommand("Lock", size - firstCounter))
    print("\n".join(str(command) for command in commandList))
    return commandList


def insertionSort(lst, commandList):
    """
    Insertion Sort Algorithm
    """
    commandList = [makeCommand("CreateList", lst)]
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
    return commandList


def quickSortCall(lst, commandList):
    """
    Call for quick sort algorithm
    """
    return quickSort(lst, 0, len(lst) - 1, commandList)


def quickSort(lst, start, end, commandList):
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
        quickSort(lst, start, left - 2, commandList)
        quickSort(lst, left, end, commandList)
    return commandList


def mergeSort(lst, commandList):
    """
    Merge Sort Algorithm
    """
    if len(lst) > 1:
        # Break the list into 2 halves and apply merge sort on them
        mid = len(lst) // 2
        leftHalf = lst[:mid]
        rightHalf = lst[mid:]
        mergeSort(leftHalf, commandList)
        mergeSort(rightHalf, commandList)
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
