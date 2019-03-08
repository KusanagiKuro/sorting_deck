#!usr#!/usr/bin/env python3
import os
import pyglet
from pyglet import text, image, resource, sprite
from cell import *


class CellGroup:
    """
    A graphic class representing a group of cells.
    """
    sizeDict = {1: 54, 2: 32, 3: 28, 4: 24, 5: 16, 6: 12, 7: 8, 8: 6}

    def __init__(self, lst, x, y):
        """
        Initialize
        Input: @lst: List. List of numbers that will be contained insde
                           the object's cells
               @x: Float. Coordinate X
               @y: Float. Coordinate Y
        """
        # Setup the coordinate. These will be the center of the group of
        # cells.
        self.x = x
        self.y = y

        # These vector determines the direction this group is moving on
        # By default, the group won't move.
        self.vectorX = 0
        self.vectorY = 0

        # Create the cells.
        indent = len(lst) / 2
        stringList = [str(integer) for integer in lst]
        maxsize = CellGroup.sizeDict.get(len(max(stringList, key=len)), 8)
        self.cells = [Cell(integer,
                           self.x - 80 * indent + 80 * index,
                           self.y,
                           maxsize,
                           index)
                      for index, integer in enumerate(lst)]
        for index, integer in enumerate(lst):
            cell = Cell(integer,
                        self.x - 80 * indent + 80 * index,
                        self.y,
                        maxsize,
                        index)
            self.cells.append(cell)
        pass

    def update(self, dt):
        for cell in self.cells:
            cell.update(dt, self.vectorX, self.vectorY)

    def draw(self):
        for cell in self.cells:
            cell.draw()

    def updateCellStatus(self, index, status):
        self.cells[index].updateStatus(status)
