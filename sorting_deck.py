#!/usr/bin/env python3
import argparse
from sort_bubble import bubbleSort
from sort_insert import insertionSort
from sort_merge_inplace import mergeSortInPlaceCall
from sort_quick import quickSortCall
from command import addCommand


def createParser():
    """
    Create a parser for the project.

    Output: parser: the parser of the project
    """
    # Create the parser
    parser = argparse.ArgumentParser(usage="sorting_deck.py [-h] [--algo ALGO]\
 [--gui] N [N ...]")

    # Create the arguments for it
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

    parser.add_argument('--algo2', nargs='?', metavar='',
                        help="specify which algorithm to use for sorting among\
[bubble|insert|quick|merge]",
                        default=None)
    return parser


def main():
    # Create the parser
    parser = createParser()

    # Parse the argument
    args = parser.parse_args()

    # If the list is too large for GUI, print out the message and exit
    if len(args.integers) > 15 and args.gui:
        print("Input too large")
        return False

    # Dictionary that contains all the sort algorithm
    algoDict = {"bubble": bubbleSort,
                "insert": insertionSort,
                "quick": quickSortCall,
                "merge": mergeSortInPlaceCall
                }

    # Create 2 command lists, 1 for each algorithm, that the GUI will run on
    commandList = []
    commandList2 = []

    # Add the initialize command to commandList
    addCommand(commandList, "Create", list(args.integers))

    # Run the algorithms
    if args.algo2:
        # Add the initialize command to commandList2
        addCommand(commandList2, "Create", list(args.integers))

        # If 2nd sort is enabled, display the type of each sort and run
        # the algorithm accordingly
        print(args.algo.capitalize() + " Sort Algorithm:")
        algoDict[args.algo](list(args.integers), commandList)
        print(args.algo2.capitalize() + " Sort Algorithm:")
        algoDict[args.algo2](list(args.integers), commandList2)

        # Add the end command to commandList2
        addCommand(commandList2, "End Result")
    else:
        # Run the algorithm accordingly.
        algoDict[args.algo](list(args.integers), commandList)

    # Add the finishing command to commandList
    addCommand(commandList, "End Result")

    # If GUI mode is enabled, run the GUI.
    if args.gui:
        from GUI import GUI
        GUI(args.algo, commandList[::-1], args.algo2, commandList2[::-1])
    return True


if __name__ == "__main__":
    main()
