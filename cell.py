#!usr#!/usr/bin/env python3
import pyglet
from math import floor
from pyglet import text, resource, sprite
from utility import createCellBorder


class Cell:
    """
    Graphic for an integer inside the list.
    Contains a border, a label representing the number and a label representing
    its index inside the list
    """
    def __init__(self, group, number, x, y,
                 fontSize, index, border="circle.png"):
        """
        Initialize the object

        Input:  @number: integer, the number inside the cell
                @x: integer, the x coordinate
                @y: integer, the y coordinate
                @fontSize: integer, the size of the label
                @index: integer, the index of the number inside the array
        """
        # x, y represent the anchor point for all of its graphic
        self.x = x
        self.y = y

        # The Cell Group that it is in
        self.group = group

        # How fast it travels on the screen
        self.speed = 0

        # The direction it's moving
        self.vectorX = 0
        self.vectorY = 0

        self.status = "normal"

        # Setup the index label, anchor point is its center
        self.index = index
        self.indexLabel = text.Label(str(self.index) if index != -1 else "",
                                     font_name="Arial",
                                     font_size=8,
                                     color=(255, 255, 0, 255),
                                     anchor_x="center",
                                     anchor_y="center",
                                     bold=True)

        # Setup the integer label, anchor point is its center
        self.number = number
        self.label = text.Label(str(number),
                                font_name="Arial",
                                font_size=fontSize,
                                color=(255, 255, 255, 255),
                                anchor_x="center",
                                anchor_y="center")

        # Setup the border by loading an image and set it anchor point to the
        # center of the image
        self.border = createCellBorder(border)

        # Setup the target list, which is where the cell will be moving
        # The order is next target = last element of the list
        # Target will be a tuple (x, y)
        self.targetList = []

        # Current target
        self.currentTarget = None

    def update(self, dt):
        """
        Update the object's coordinate

        Input:  @dt: tick of the clock. Passed by the schedule_interval.
                @listVectorX: integer, horizontal movement of the list.
                @listVectorY: integer, vertical movement of the list.
        """
        # If the list is moving, update the cell's coordinate accordingly
        try:
            if self.group.vectorX or self.group.vectorY:
                self.x += self.speed * self.group.vectorX
                self.y += self.speed * self.group.vectorY

            # Else update it by its vector
            else:
                self.x += self.speed * self.vectorX
                self.y += self.speed * self.vectorY
        except AttributeError:
            self.x += self.speed * self.vectorX
            self.y += self.speed * self.vectorY

        # Move the border and 2 labels accordingly
        self.border.set_position(self.x, self.y)
        self.label.x = self.x
        self.label.y = self.y + 2
        self.indexLabel.x = self.x
        self.indexLabel.y = self.y - 40

        # Check if it has reached the target, choose a next one if needed
        if self.checkTarget() and self.targetList:
            self.getNewTarget()

        if len(self.targetList) == 0 and self.currentTarget is None:
            return False
        else:
            return True

    def draw(self):
        """
        Draw the cell, border first, then the number inside, then the index
        """
        self.border.draw()
        self.label.draw()
        self.indexLabel.draw()
        self.update(0)

    def getNewTarget(self):
        """
        Get a new target from the target list
        """
        self.currentTarget = self.targetList.pop()
        self.getDirection()

    def getDirection(self):
        """
        Get the direction for the cell to move to its target
        """
        if self.currentTarget[0] > self.x:
            # Move Right
            self.vectorX = 1
            self.speed = floor(abs(self.currentTarget[0] - self.x) / 48)
        elif self.currentTarget[0] < self.x:
            # Move Left
            self.vectorX = -1
            self.speed = floor(abs(self.currentTarget[0] - self.x) / 48)
        elif self.currentTarget[1] > self.y:
            # Move Up
            self.vectorY = 1
            self.speed = floor(abs(self.currentTarget[1] - self.y) / 48)
        elif self.currentTarget[1] < self.y:
            # Move Down
            self.vectorY = -1
            self.speed = floor(abs(self.currentTarget[1] - self.y) / 48)

    def moveRightby1(self):
        """
        Move the cell to the right by 1 index.
        """
        self.addTarget([(self.x + 96, self.y)])
        self.setIndex(self.index + 1)

    def checkTarget(self):
        """
        Check if the cell has reached its target

        Output: True if it doesn't have the target or has reached its target.
                False otherwise.
        """
        if not self.currentTarget:
            return True
        # If the cell has reached the target, reset its vector and reposition
        # it to the correct coordinate, then return true
        if ((self.vectorX > 0 and self.x >= self.currentTarget[0]) or
                (self.vectorX < 0 and self.x <= self.currentTarget[0])):
            self.vectorX = 0
            self.x = self.currentTarget[0]
            self.currentTarget = None
            return True
        elif ((self.vectorY > 0 and self.y >= self.currentTarget[1]) or
                (self.vectorY < 0 and self.y <= self.currentTarget[1])):
            self.vectorY = 0
            self.y = self.currentTarget[1]
            self.currentTarget = None
            return True
        return False

    def addTarget(self, targets):
        """
        Add targets to the cell's target list

        Input: @targets: list of 2-integer tuples, representing the x y
                         coordinate of the targets
        """
        self.targetList += targets
        return True

    def instantMove(self):
        """
        Instantly move to the current target.
        """
        self.x = self.currentTarget[0]
        self.y = self.currentTarget[1]

    def setVisible(self, visible):
        """
        Set the visibility of the cell

        Input: @visible: Boolean.
        """
        if visible:
            self.indexLabel.text = str(self.index) if self.index != -1 else ""
            self.label.text = str(self.number)
        else:
            self.indexLabel.text = ""
            self.label.text = ""
        self.border.visible = visible

    def setPosition(self, x, y):
        """
        Set the position of the cell

        Input: @x: int. The x coordinate
               @y: int. The y coordinate
        """
        self.x = x
        self.y = y

    def setValue(self, integer):
        """
        Set the value of the cell and edit its label accordingly
        Input: @integer: int. The new value of the cell.
        """
        self.number = integer
        self.label.text = str(integer)

    def setIndex(self, index):
        """
        Set the index of the cell and edit its index label accordingly

        Input: @index: integer. The new index of the cell
        """
        self.index = index
        self.indexLabel.text = str(index)

    def setBorder(self, border=None):
        """
        Set the border of the cell and edit its accordingly

        Input: @border: string. The path of the new border
        """
        self.border = createCellBorder(border)
        self.border.draw()
        self.update(0)

    def setStatus(self, status):
        """
        Set the status of the cell, showed by changing the border

        Input:  @status: string.
        """
        # Dictionary contains all the borders according to the status
        borderDict = {"sorted": "sortedcircle.png",
                      "compare": "tealcircle.png",
                      "normal": "circle.png",
                      "confirmed": "greencircle.png",
                      "mark": "purplecircle.png",
                      "locked": "blackcircle.png"}

        # Change the border
        self.setBorder(borderDict[status])

        # Change the status
        self.status = status
