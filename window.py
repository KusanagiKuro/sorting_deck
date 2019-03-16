#!usr#!/usr/bin/env python3
import pyglet
from cellgroup import *
from pyglet import text, resource, sprite
from utility import *
from cell import *
from actionmenu import *
from pyglet.window import key


class Window(pyglet.window.Window):
    def __init__(self, commandList, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Non-graphic attributes
        # List of commands
        self.commands = commandList

        # List of cell group for 1st algorithm
        self.groupList1 = []

        # List of cell group for 2nd algorithm
        self.groupList2 = []

        # Current cell group being worked on
        self.currentCellGroup = None

        # Current state
        self.isExecuting = False

        # Is manual mode on
        self.manualMode = True

        # Background setup
        background = resource.image("background.png")
        self.background = sprite.Sprite(background)
        self.background.scale_x = self.width / background.width
        self.background.scale_y = self.height / background.height

        # Glossary Menu setup
        self.glossaryMenu = createMenu(400, 600, self.width - 200, 300)

        # Action Menu setup
        self.actionMenu = ActionMenu(self.width, self.height)

        # Input label setup
        self.inputLabel = text.Label()

        # Markers for quick sort
        self.markers = []

    def on_draw(self):
        """
        Draw the window and all of its components
        """

        # Clear out the window.
        self.clear()

        # Draw the background
        self.background.draw()

        # Draw the glossary menu
        self.glossaryMenu.draw()

        # Draw the action menu
        self.actionMenu.draw()

        # Draw all the cell groups
        for cellGroup in self.groupList1:
            cellGroup.draw()

        # Draw all the markers
        for marker in self.markers:
            marker.draw()

    def on_key_press(self, symbol, modifier):
        """
        Detect certain key press and react accordingly

        Input: @symbol: key. The key press.
               @modifier: addtional modifier, like SHIFT, ALT, CTRL
        """
        # If the key press is SPACE, switch between manual and auto mode.
        if symbol == key.SPACE:
            self.switchMode()

        # If the key press is ENTER, switch to manual mode and execute the next
        # command if the window isn't executing any command.
        elif symbol == key.ENTER:
            if not self.manualMode:
                self.manualMode = True
            elif not self.isExecuting:
                self.executeNextCommand()

        # If the key press is ESCAPE, exit the program
        elif symbol == key.ESCAPE:
            pyglet.app.exit()

    def update(self, dt):
        # If the window isn't executing any command and is in auto mode,
        # execute next command.
        if not self.isExecuting and not self.manualMode:
            self.executeNextCommand()

        # Set the current state accordingly to the execution of the components
        # This is True if any component is still in execution
        # Only False if all components aren't in execution
        self.isExecuting = any([cellGroup.update(dt)
                                for cellGroup in self.groupList1])

    def executeNextCommand(self):
        """
        Execute the next command in the command list
        """

        # List of functions for each type of command
        functionDic = {"Create": self.createList,
                       "Compare": self.compareCells,
                       "Swap": self.swapCells,
                       "Shift": self.shiftCells,
                       "Split": self.splitGroup,
                       "UpdateStatus": self.updateCellStatus,
                       "CreateMarkers": self.createMarker,
                       "MoveLeftMarker": self.moveMarker,
                       "MoveRightMarker": self.moveMarker,
                       "End Result": self.displayEndResult,
                       "Exit": self.exit
                       }
        # Pop the next command from the command list
        command = self.commands.pop()

        # Call the respective function with the type of the function
        functionDic[command[0]](command[1])
        self.actionMenu.executeCommand(command)

        # Set this variable to True so that the two commands will never overlap
        # Except the UpdateStatus command
        if command[0] != "UpdateStatus":
            self.isExecuting = True
        else:
            self.executeNextCommand()

    def createList(self, lst):
        """
        Graphic display for creating a new list.
        Input: @lst: List of integers.
        """
        # New cell group, representing the new list
        newCellGroup = CellGroup(lst[0], (self.width - 300) // 2,
                                 self.height-150*(len(self.groupList1)+1))

        # Add the new cell group to the group list
        self.groupList1.append(newCellGroup)

        # Set the new group to become the current working group
        self.currentCellGroup = newCellGroup

    def updateCellStatus(self, lst):
        """
        Pass the parameters to the current working cell group to swap cell.
        """
        for index in lst[0]:
            self.currentCellGroup.updateCellStatus(index, lst[1])

    def swapCells(self, lst):
        """
        Pass the parameters to the current working cell group to swap cell.
        """
        self.currentCellGroup.swapCells(lst)

    def compareCells(self, lst):
        """
        Compare the two cell in the current Cell List

        Input: @lst: list of integer. represent the index of the number
        """
        # Set the status of the two cells to compare
        for index in lst[:2]:
            if index >= 0:
                self.currentCellGroup.updateCellStatus(index, "compare")

    def exit(self, lst=None):
        """
        Exit the program
        """
        pyglet.app.exit()

    def returnCells(self, lst):
        """
        Pass the parameters to the current working cell group to return
        a list of cells back to its group.

        Input: @lst: list of integer. represent the index of the number
        """
        for index in lst:
            self.currentCellGroup.returnCell(index)

    def displayEndResult(self, lst):
        """
        Display the result of the sort.

        Input: @lst: Empty list.
        """
        # Set all the cells to confirmed status.
        self.updateCellStatus([[index for index in
                                range(self.currentCellGroup.len())],
                               "confirmed"])

        # Turn on manual mode so the user can take a look at the end result.
        self.manualMode = True

    def shiftCells(self, lst):
        """
        Pass the parameters to the current working cell group to shift all
        cells between two position to the right by 1 index.

        Input: @lst: list of integer.
        """
        self.currentCellGroup.shiftCells(lst)

    def switchMode(self, dt=None):
        """
        Switching between manual mode and auto mode
        """
        self.manualMode = not self.manualMode

    def splitGroup(self, lst):
        """
        Visualise the split of the group

        Input: @lst: list of integer. Contains the start, the end of the
               list and the split point.
        """
        start, mid, end = lst[0], lst[1], lst[2]
        # All the cells in 1st part will be marked with normal status
        self.updateCellStatus([[index for index in range(start, mid)],
                               "normal"])

        # All the cells in 2nd part will be marked with mark status
        self.updateCellStatus([[index for index in range(mid, end)],
                               "mark"])

        # All other cells will be marked with locked status
        self.updateCellStatus([[index for index in
                                range(self.currentCellGroup.len())
                                if index < start or index >= end],
                               "locked"])

    def createMarker(self, lst):
        """
        Create the marker for pivot and for other tracker.

        Input: @lst: list of integer. Contains the index that the new marker
                     point to.
        """
        if len(self.markers) == 3:
            for index in range(3):
                print(index)
                self.moveMarker([index, lst[index]])
            return
        for index in lst:
            print(index)
            newMarker = (createSprite("arrow.png") if len(self.markers) < 2
                         else createSprite("bluearrow.png"))
            newMarker.x = self.currentCellGroup.cells[index].x
            newMarker.y = (self.currentCellGroup.cells[index].y - 80
                           if len(self.markers) < 2 else
                           self.currentCellGroup.cells[index].y + 80)
            newMarker.scale = 0.05
            newMarker.rotation = (180 if len(self.markers) < 2 else 0)
            self.markers.append(newMarker)

    def moveMarker(self, lst):
        """
        Move the marker to the new position

        Input: @lst: list of intger. Contains the marker index and the index
               of the new position
        """
        self.markers[lst[0]].x = self.currentCellGroup.cells[lst[1]].x
        self.markers[lst[0]].y = (self.currentCellGroup.cells[lst[1]].y - 80
                                  if lst[0] != 2 else
                                  self.currentCellGroup.cells[lst[1]].y + 80)
