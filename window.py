#!usr#!/usr/bin/env python3
import pyglet
from cellgroup import CellGroup
from pyglet import text, resource, sprite
from utility import createSprite
from cell import Cell
from actionmenu import ActionMenu
from pyglet.window import key


class Window(pyglet.window.Window):
    def __init__(self, sortalgo, commandList, sortalgo2, commandList2,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Non-graphic attributes
        # List of commands
        self.commands = ([commandList, commandList2] if commandList2 else
                         [commandList])

        # List of Cell Group
        self.cellGroup = []

        # List of Algo:
        self.algo = [sortalgo, sortalgo2]

        # Current state
        self.Executing = [False, False]

        # Is manual mode on
        self.manualMode = True

        # Background setup
        background = resource.image("background.png")
        self.background = sprite.Sprite(background)
        self.background.scale_x = self.width / background.width
        self.background.scale_y = self.height / background.height

        # Action Menu setup
        self.actionMenu = []

        # Markers for quick sort
        self.markers = [[], []]

    def on_draw(self):
        """
        Draw the window and all of its components
        """

        # Clear out the window.
        self.clear()

        # Draw the background
        self.background.draw()

        # Draw the action menu
        for menu in self.actionMenu:
            menu.draw()

        # Draw all the cell groups
        for cellGroup in self.cellGroup:
            cellGroup.draw()

        # Draw all the markers
        for listmarker in self.markers:
            for marker in listmarker:
                marker.draw()

    def on_key_press(self, symbol, modifier):
        """
        Detect certain key press and react accordingly

        Input: @symbol: key. The key press.
               @modifier: addtional modifier, like SHIFT, ALT, CTRL
        """
        # SPACE will switch between manual and auto mode.
        if symbol == key.SPACE:
            self.switchMode()

        # ENTER will switch to manual mode and execute the next
        # command in command list 1 if the window isn't executing any command.
        elif symbol == key.ENTER:
            if not self.manualMode:
                self.manualMode = True
            if not self.Executing[0]:
                self.executeNextCommand(0)

        elif symbol == key.RIGHT and len(self.cellGroup) == 2:
            if not self.manualMode:
                self.manualMode = True
            if not self.Executing[1]:
                self.executeNextCommand(1)

        # If the key press is ESCAPE, exit the program
        elif symbol == key.ESCAPE:
            pyglet.app.exit()

    def switchMode(self):
        """
        Switching between manual mode and auto mode
        """
        self.manualMode = not self.manualMode

    def update(self, dt):
        # If the window isn't executing any command and is in auto mode,
        # execute next command.
        if not self.cellGroup:
            for order in range(len(self.commands)):
                command = self.getCommand(order)
                self.createList(command[1])
                self.createActionMenu(order)
        else:
            for order in range(len(self.cellGroup)):
                if not self.Executing[order] and not self.manualMode:
                    self.executeNextCommand(order)
                self.isExecuting(order)

    def isExecuting(self, order):

        # Set the current state accordingly to the execution of
        # the components
        # This is True if any component is still in execution
        # Only False if all components aren't in execution
        self.Executing[order] = (any(self.actionMenu[order].update())
                                 or
                                 any([self.cellGroup[order].update()]))

    def getCommand(self, order):
        return self.commands[order].pop()

    def createList(self, lst):
        """
        Graphic display for creating a new list.
        Input: @lst: List of integers.
        """
        # New cell group, representing the new list
        newCellGroup = CellGroup(lst[0], (self.width - 300) // 2,
                                 self.height-240 -
                                 480*len(self.cellGroup))

        # Add the new cell group to the group list
        self.cellGroup.append(newCellGroup)

    def createActionMenu(self, order):
        """
        """
        newActionMenu = ActionMenu(self.algo[order], self.width,
                                   self.height-480*order)
        self.actionMenu.append(newActionMenu)

    def executeNextCommand(self, order):
        """
        Execute the next command in the command list
        """
        if not self.commands[order]:
            return
        # List of functions for each type of command
        functionDic = {"Compare": self.compareCells,
                       "Swap": self.swapCells,
                       "Shift": self.shiftCells,
                       "Split": self.splitGroup,
                       "UpdateStatus": self.updateCellStatus,
                       "CreateMarkers": self.createMarker,
                       "HideMarkers": self.hideMarker,
                       "MoveLeftMarker": self.moveMarker,
                       "MoveRightMarker": self.moveMarker,
                       "End Result": self.displayEndResult,
                       "Exit": self.exit
                       }
        # Pop the next command from the command list
        command = self.getCommand(order)

        # Call the respective function with the type of the function
        functionDic[command[0]](order, command[1])
        self.actionMenu[order].executeCommand(command)

        # Set this variable to True so that the two commands will never overlap
        # Except the UpdateStatus command
        if command[0] != "UpdateStatus":
            self.Executing[order] = True
        else:
            self.executeNextCommand(order)

    def updateCellStatus(self, order, lst):
        """
        Pass the parameters to the current working cell group to swap cell.
        """
        for index in lst[0]:
            self.cellGroup[order].updateCellStatus(index, lst[1])

    def swapCells(self, order, lst):
        """
        Pass the parameters to the current working cell group to swap cell.
        """
        self.cellGroup[order].swapCells(lst)

    def compareCells(self, order, lst):
        """
        Compare the two cell in the current Cell List

        Input: @lst: list of integer. represent the index of the number
        """
        # Set the status of the two cells to compare
        for index in lst[:2]:
            self.cellGroup[order].updateCellStatus(index, "compare")

    def exit(self, lst=None):
        """
        Exit the program
        """
        pyglet.app.exit()

    def returnCells(self, order, lst):
        """
        Pass the parameters to the current working cell group to return
        a list of cells back to its group.

        Input: @lst: list of integer. represent the index of the number
        """
        for index in lst:
            self.cellGroup[order].returnCell(index)

    def displayEndResult(self, order, lst):
        """
        Display the result of the sort.

        Input: @lst: Empty list.
        """
        # Set all the cells to confirmed status.
        self.updateCellStatus(order,
                              [[index for index in
                                range(self.cellGroup[order].len())],
                               "confirmed"])

        # Hide all the markers
        self.hideMarker(order, lst)

        # Turn on manual mode so the user can take a look at the end result.
        self.manualMode = all([True if commandList else False
                               for commandList in self.commands])

    def shiftCells(self, order, lst):
        """
        Pass the parameters to the current working cell group to shift all
        cells between two position to the right by 1 index.

        Input: @lst: list of integer.
        """
        self.cellGroup[order].shiftCells(lst)

    def splitGroup(self, order, lst):
        """
        Visualise the split of the group

        Input: @lst: list of integer. Contains the start, the end of the
               list and the split point.
        """
        start, mid, end = lst[0], lst[1], lst[2]
        # All the cells in 1st part will be marked with normal status
        self.updateCellStatus(order,
                              [[index for index in range(start, mid)],
                               "normal"])

        # All the cells in 2nd part will be marked with mark status
        self.updateCellStatus(order,
                              [[index for index in range(mid, end)],
                               "mark"])

        # All other cells will be marked with locked status
        self.updateCellStatus(order,
                              [[index for index in
                                range(self.cellGroup[order].len())
                                if index < start or index >= end],
                               "locked"])

    def createMarker(self, order, lst):
        """
        Create the marker for pivot and for other tracker.

        Input: @lst: list of integer. Contains the indexes that the new markers
                     point to.
        """
        # If all the markers have been created, move them instead of creating
        # new one
        if self.markers[order]:
            for index in range(3):
                self.moveMarker(order, [index, lst[index]])
                self.markers[order][index].visible = True
            return
        # Dictionary contains the value that are needed to create the marker
        valueDict = {0: ("redarrow.png", -96),
                     1: ("bluearrow.png", -96),
                     2: ("arrow.png", 96)}
        for index, position in enumerate(lst):
            newMarker = createSprite(valueDict[index][0])
            newMarker.x = (self.cellGroup[order].x -
                           96 * self.cellGroup[order].indent +
                           96 * position)
            newMarker.y = self.cellGroup[order].y + valueDict[index][1]
            newMarker.scale = 0.015
            self.markers[order].append(newMarker)

    def hideMarker(self, order, lst):
        """
        Hide all the markers
        """
        for marker in self.markers[order]:
            marker.visible = False

    def moveMarker(self, order, lst):
        """
        Move the marker to the new position

        Input: @lst: list of integer. Contains the marker index and the index
               of the new position
        """
        self.markers[order][lst[0]].x = (self.cellGroup[order].x -
                                         96 * self.cellGroup[order].indent +
                                         96 * lst[1])
        self.markers[order][lst[0]].y = (self.cellGroup[order].y - 80
                                         if lst[0] != 2 else
                                         self.cellGroup[order].y + 80)
