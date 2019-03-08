#!usr#!/usr/bin/env python3
import os
import pyglet
from math import floor
from pyglet import text, image, resource, sprite
from pyglet.window import Window, key
from utility import *
from cell import *


class CellList:
    sizeDict = {1: 54, 2: 32, 3: 28, 4: 24, 5: 16, 6: 12, 7: 8, 8: 6}

    def __init__(self, lst, x, y):
        self.cells = []
        self.lst = lst
        self.x = x
        self.y = y
        self.vectorX = 0
        self.vectorY = 0
        indent = len(self.lst) / 2
        stringList = [str(integer) for integer in lst]
        maxsize = CellList.sizeDict.get(len(max(stringList, key=len)), 8)
        for index, integer in enumerate(self.lst):
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
