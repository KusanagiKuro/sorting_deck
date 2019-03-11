#!usr#!/usr/bin/env python3
import os
import pyglet
from math import floor
from pyglet import text, image, resource, sprite
from utility import createBorder


def swap(cell1, cell2):
    cell1.addTarget([(cell2.x, cell2.y),
                     (cell2.x, cell2.y + 80)
                     (cell1.x, cell2.y + 80)])
    cell2.addTarget([(cell1.x, cell1.y),
                     (cell1.x, cell1.y - 80)
                     (cell2.x, cell1.y - 80)])
    swapValue(cell1.indexlabel.text, cell2.indexlabel.text)
    return True


class Cell:
    """
    Graphic for an integer inside the list.
    Contains a border, a label representing the number and a label representing
    its index inside the list
    """
    def __init__(self, number, x, y, fontSize, index, border=None):
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

        # How fast it travels on the screen
        self.speed = 0

        # The direction it's moving
        self.vectorX = 0
        self.vectorY = 0

        # Setup the index label, anchor point is its center
        self.index = index
        self.indexlabel = text.Label(str(self.index) if index >= 0 else "",
                                     font_name="Arial",
                                     font_size=8,
                                     color=(255, 255, 0, 255),
                                     anchor_x="center",
                                     anchor_y="center",
                                     bold=True)

        # Setup the integer label, anchor point is its center
        self.label = text.Label(str(number),
                                font_name="Arial",
                                font_size=fontSize,
                                color=(255, 255, 255, 255),
                                anchor_x="center",
                                anchor_y="center")

        # Setup the border by loading an image and set it anchor point to the
        # center of the image
        self.border = createBorder() if not border else createBorder(border)
        self.border.scale = 80 / 1265 * 1.4

        # Setup the target list, which is where the cell will be moving
        # The order is next target = last element of the list
        # Target will be a tuple (x, y)
        self.targetList = []

        # Current target
        self.currentTarget = None

    def update(self, dt, listVectorX=0, listVectorY=0):
        """
        Update the object's coordinate
        Input:  @dt: tick of the clock. Passed by the schedule_interval.
                @listVectorX: integer, horizontal movement of the list.
                @listVectorY: integer, vertical movement of the list.
        """
        # If the list is moving, update the cell's coordinate accordingly
        if listVectorX or listVectorY:
            self.x += self.speed * listVectorX
            self.y += self.speed * listVectorY

        # Else update it by its vector
        else:
            self.x += self.speed * self.vectorX
            self.y += self.speed * self.vectorY

        # Move the border and 2 labels accordingly
        self.border.set_position(self.x, self.y)
        self.label.x = self.x
        self.label.y = self.y + 2
        self.indexlabel.x = self.x
        self.indexlabel.y = self.y - 33

        # Check if it has reached the target, choose a next one if needed
        self.updateTarget()

    def draw(self):
        """
        Draw the cell, with its border first, then the number inside, then
        the index
        """
        self.border.draw()
        self.label.draw()
        self.indexlabel.draw()
        self.update(0)

    def updateTarget(self):
        """
        If the cell has reached its target, get the next one if the target list
        isn't empty
        """
        if not self.currentTarget and self.targetList:
            self.currentTarget = self.targetList.pop()
        self.getDirection()

    def getDirection(self):
        """
        Get the direction for the cell to move to its target
        """
        print(self.currentTarget)
        if not self.currentTarget:
            self.vectorX = 0
            self.vectorY = 0
        elif self.currentTarget[0] > self.x:
            # Move Right
            self.vectorX = 1
            self.speed = floor(abs(self.currentTarget[0] - self.x) / 30)
        elif self.currentTarget[0] < self.x:
            # Move Left
            self.vectorX = -1
            self.speed = floor(abs(self.currentTarget[0] - self.x) / 30)
        elif self.currentTarget[1] > self.y:
            # Move Up
            self.vectorY = 1
            self.speed = floor(abs(self.currentTarget[1] - self.y) / 30)
        elif self.currentTarget[1] < self.y:
            # Move Down
            self.vectorY = -1
            self.speed = floor(abs(self.currentTarget[1] - self.y) / 30)

    def updateStatus(self, status):
        """
        Update the status of the cell, showed by changing the border
        Input:  @status: string. Choose from "sorted", "compare", "locked"
        """
        if status == "sorted":
            self.border.delete()
            self.border = createBorder("sortedcircle.png")
            self.border.scale = 80 / 1265 * 1.4
        elif status == "compare":
            self.targetList.append((self.x, self.y + 90))
        elif status == "unsorted":
            self.border.delete()
            self.border = createBorder("circle.png")
            self.border.scale = 80 / 1265 * 1.4
        self.draw()

    def addTarget(self, targets):
        """
        Add targets to the cell's target list
        Input: @targets: list of tuple of 2 integers, representing the x y
                         coordinate of the target
        """
        self.targetList += targets
        return True

    def getValue(self):
        return self.label.text

    def getIndex(self):
        return self.indexlabel.text
