#!usr#!/usr/bin/env python3


def makeCommand(lst, name, *args):
    """
    Make a command and add it to the list.

    Structure of a command:

    A 2-element tuple.
    1st element: string, the type of the command
    2nd element: list, things that are needed as parameters
                 for the respective function of that command

    Types of command and their parameters:
    - Create:
      List of integers, represent the list that will be created

    - Compare:
      4-element list.
      1st element: the index of first number
      2nd element: the index of second number
      3rd element: the value of first number
      4th element: the value of second number
      5th element: the condition that we are checking

    - Swap:
      1st element: the index of first number
      2nd element: the index of second number

    - UpdateStatus:
      List of integers, represent the index of the cells whose status will be
      changed.

    - Return:
      List of integers, represent the index of the numbers that will return to
      their position

    - Shift:
      2-element list.
      1st element: the base index
      2nd element: the index of the destination

    - Split:
      2-element list.

    - Confirm:
      Empty list.

    - Exit:
      Empty list
    """
    lst.append((name, args))
