#!/usr/bin/env python3
import argparse
from bubblesort import *
from quicksort import *
from insertionsort import *
from mergesort import *
from utility import *


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
    gui = None
    if args.gui:
        if len(args.integers) > 15:
            print("Input too large")
            return
        else:
            import pyglet
            gui = open("res/command.txt", "rw")
    algoDict[args.algo](args.integers, args.gui)
    if args.gui:
        GUI()
        gui.close()


if __name__ == "__main__":
    main()
