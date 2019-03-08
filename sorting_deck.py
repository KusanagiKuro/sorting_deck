#!/usr/bin/env python3
import argparse
from sort import *
from utility import *
from GUI import *


def createParser():
    usageText = ""
    parser = argparse.ArgumentParser(usage="sorting_deck.py [-h] [--algo ALGO]\
 [--gui] N [N ...]")
    parser.add_argument('--algo', nargs='?', metavar='',
                        help="specify which algorithm to use for sorting among\
 [bubble|insert|quick|merge], default bubble",
                        action="store",
                        choices=["bubble", "insert", "quick", "merge"],
                        default="bubble")
    parser.add_argument('--gui', action="store_true",
                        help="visualise the algorithm in GUI mode")
    parser.add_argument('integers', metavar="N", nargs='+', type=int,
                        help="an integer for the list to sort")
    return parser


def main():
    parser = createParser()
    args = parser.parse_args()
    algoDict = {"bubble": bubbleSort,
                "insert": insertionSort,
                "quick": quickSortCall,
                "merge": mergeSort}
    commandList = algoDict[args.algo](args.integers, args.gui)
    if args.gui:
        if len(args.integers) > 15:
            print("Input too large")
            return False
        else:
            import pyglet
        commandList.append(makeCommand("Exit"))
        GUI(commandList[::-1])
        gui.close()
    return True


if __name__ == "__main__":
    main()
