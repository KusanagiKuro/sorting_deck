#!/usr/bin/env python3
import argparse
from sort_bubble import bubbleSort
from sort_insert import insertionSort
from sort_merge_inplace import mergeSortInPlaceCall
from sort_merge_outofplace import mergeSort
from sort_quick import quickSortCall
from command import makeCommand
from GUI import GUI


def createParser():
    parser = argparse.ArgumentParser(usage="sorting_deck.py [-h] [--algo ALGO]\
 [--gui] N [N ...]")
    parser.add_argument('--algo', nargs='?', metavar='',
                        help="specify which algorithm to use for sorting among\
 [bubble|insert|quick|merge], default bubble",
                        action="store",
                        choices=["bubble", "insert", "quick", "merge",
                                 "mergeinplace"],
                        default="bubble")
    parser.add_argument('--gui', action="store_true",
                        help="visualise the algorithm in GUI mode")
    parser.add_argument('integers', metavar="N", nargs='+', type=int,
                        help="an integer for the list to sort")
    return parser


def main():
    # Create the parser
    parser = createParser()

    # Parse the argument
    args = parser.parse_args()

    # Dictionary that contains all the sort algorithm
    algoDict = {"bubble": bubbleSort,
                "insert": insertionSort,
                "quick": quickSortCall,
                "merge": mergeSort,
                "mergeinplace": mergeSortInPlaceCall}

    # The command list that the GUI will run on
    commandList = []
    makeCommand(commandList, "Create", list(args.integers))

    # Run the algorithm accordingly.
    algoDict[args.algo](args.integers, commandList)

    # Run the GUI if needed
    if args.gui:
        if len(args.integers) > 15:
            print("Input too large")
            return False
        else:
            import pyglet
        makeCommand(commandList, "End Result")
        makeCommand(commandList, "Exit")
        GUI(commandList[::-1])
    return True


if __name__ == "__main__":
    main()
