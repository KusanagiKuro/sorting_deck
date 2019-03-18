#!usr#!/usr/bin/env python3
from pyglet import text
from cell import Cell


class CellGroup:
    """
    A graphic class representing a group of cells.
    """
    sizeDict = {1: 48, 2: 32, 3: 28, 4: 24, 5: 16, 6: 12, 7: 8, 8: 6}

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
        self.indent = len(lst) / 2
        stringList = [str(integer) for integer in lst]
        maxsize = CellGroup.sizeDict.get(len(max(stringList, key=len)), 8)
        self.cells = [Cell(self,
                           integer,
                           self.x - 96 * self.indent + 96 * index,
                           self.y,
                           maxsize,
                           index)
                      for index, integer in enumerate(lst)]

    def update(self):
        return any([cell.update() for cell in self.cells])

    def draw(self):
        for cell in self.cells:
            cell.draw()

    def len(self):
        return len(self.cells)

    def updateCellStatus(self, index, status):
        """
        Update the status of a cell

        Input: @index: integer. The index of the cell.
               @status: string. The new status
        """
        self.cells[index].setStatus(status)

    def swapCells(self, lst):
        """
        Swap the position and index of 2 cells.

        Input: @lst: list of 2 tuples, representing the index of the cells.
        """
        cell1 = self.cells[lst[0]]
        cell2 = self.cells[lst[1]]
        targetList1 = [(cell2.x, cell1.y)]
        cell1.addTarget([(cell2.x, cell1.y)])
        cell2.addTarget([(cell1.x, cell2.y)])
        cell1.setIndex(lst[1])
        cell2.setIndex(lst[0])
        self.cells[lst[0]] = cell2
        self.cells[lst[1]] = cell1

    def shiftCells(self, lst):
        """
        Shift all cells between the base index and the destination to the right
        by 1 unit

        Input: @lst: List of 2 integers.
        """
        # Set a variable to the base index cell so we don't lose it
        key = self.cells[lst[0]]

        # For every cell within the range of destination and base index, shift
        # to the right.
        for index in range(lst[0] - 1, lst[1] - 1, -1):
            self.cells[index].moveRightby1()

            # Set the index of the cell to its new position
            self.cells[index].setIndex(index + 1)

            # Update its position in the cell group
            self.cells[index + 1] = self.cells[index]

        # Setup the path for the key cell
        destination = (self.cells[lst[0]].x - 96 * (lst[0] - lst[1] - 1),
                       self.cells[lst[0]].y)

        # Order it to move there
        key.addTarget([destination])

        # Set its index and update its position in the cell group
        key.setIndex(lst[1])
        self.cells[lst[1]] = key

        # Set the status of the key cell back to normal
        key.setStatus("normal")
