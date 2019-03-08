#!usr#!/usr/bin/env python3
import os
import pyglet
from cellgroup import *
from pyglet import text, image, resource, sprite
from utility import *
from cell import *


class Window(pyglet.window.Window):
    def __init__(self, commandList, width=None, height=None, caption=None,
                 resizable=False, style=None, fullscreen=False,
                 visible=True, vsync=True, display=None,
                 screen=None, config=None, context=None, mode=None):
        super().__init__(width, height, caption, resizable, style,
                         visible, vsync, display, screen, config,
                         context, mode)
        self.commands = commandList
        self.groupList = []
        self.currentCellList = None
        background = resource.image("background.png")
        self.background = sprite.Sprite(background)
        self.background.scale_x = self.width / background.width
        self.background.scale_y = self.height / background.height
        self.border = createBorder()
        self.border.scale = 80 / 64
        self.glossaryBorder = createBorder("rectangle.png")
        self.glossaryBorder.scale = 1.5
        self.glossaryBorder.x = self.width - 150
        self.glossaryBorder.y = 300
        self.inputLabel = text.Label()
        self.isInExecuted = False

    def on_draw(self):
        self.clear()
        self.background.draw()
        self.glossaryBorder.draw()
        for cellList in self.groupList:
            cellList.draw()

    def on_key_press(self, symbol, modifier):
        if symbol == key.SPACE:
            self.isInExecuted = False
        elif symbol == key.ESCAPE:
            pyglet.app.exit()

    def update(self, dt):
        self.executeNextCommand()
        for cellList in self.groupList:
            cellList.update(dt)

    def executeNextCommand(self):
        if not self.isInExecuted:
            functionDic = {"CreateList": self.createList,
                           "Lock": self.lockCell,
                           "Swap": self.swapCells,
                           "Result": self.showResult,
                           "Compare": self.compareCells,
                           "Exit": self.exit
                           }
            components = self.commands.pop()
            functionDic[components[0]](components[1])
            self.isInExecuted = True

    def createList(self, lst):
        newCellList = CellList(lst[0], (self.width - 150) // 2,
                               self.height - 150 * (len(self.groupList) + 1))
        self.groupList.append(newCellList)
        self.currentCellList = newCellList

    def lockCell(self, lst):
        pass

    def swapCells(self, lst):
        pass

    def showResult(self, lst):
        pass

    def compareCells(self, lst):
        """
        Compare the two cell in the current Cell List
        Input: @lst: List. First element represent the index of first number,
                     Second element represent the index of second number
        """
        self.currentCellList.updateCellStatus(lst[0], "compare")
        self.currentCellList.updateCellStatus(lst[1], "compare")
        pass

    def exit(self, lst):
        pyglet.app.exit()
