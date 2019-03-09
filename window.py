#!usr#!/usr/bin/env python3
import os
import pyglet
from cellgroup import *
from pyglet import text, image, resource, sprite
from utility import *
from cell import *
from actionmenu import *
from pyglet.window import key


class Window(pyglet.window.Window):
    def __init__(self, commandList, width=None, height=None, caption=None,
                 resizable=False, style=None, fullscreen=False,
                 visible=True, vsync=True, display=None,
                 screen=None, config=None, context=None, mode=None):
        super().__init__(width, height, caption, resizable, style,
                         visible, vsync, display, screen, config,
                         context, mode)
        # Non-graphic attributes
        # List of commands
        self.commands = commandList

        # List of cell group
        self.groupList = []

        # Current cell group being worked on
        self.currentcellGroup = None

        # Current state
        self.isExecuting = False

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

    def on_draw(self):
        self.clear()
        self.background.draw()
        self.glossaryMenu.draw()
        self.actionMenu.draw()
        for cellGroup in self.groupList:
            cellGroup.draw()

    def on_key_press(self, symbol, modifier):
        if symbol == key.SPACE:
            self.isExecuting = False
        elif symbol == key.ESCAPE:
            pyglet.app.exit()

    def update(self, dt):
        if not self.isExecuting:
            self.executeNextCommand()
        for cellGroup in self.groupList:
            cellGroup.update(dt)

    def executeNextCommand(self):
        self.isExecuting = True
        functionDic = {"Create": self.createList,
                       "Lock": self.lockCell,
                       "Swap": self.swapCells,
                       "Result": self.showResult,
                       "Compare": self.compareCells,
                       "Exit": self.exit
                       }
        command = self.commands.pop()
        functionDic[command[0]](command[1])
        self.updateMenus(command)

    def createList(self, lst):
        newcellGroup = CellGroup(lst, (self.width - 400) // 2,
                                 self.height - 150 * (len(self.groupList) + 1))
        self.groupList.append(newcellGroup)
        self.currentcellGroup = newcellGroup

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
        self.currentcellGroup.updateCellStatus(lst[0], "compare")
        self.currentcellGroup.updateCellStatus(lst[1], "compare")
        pass

    def exit(self, lst):
        pyglet.app.exit()

    def updateMenus(self, command):
        self.actionMenu.updateCommand(command)
        pass

    # def setupActionMenu(self):
    #     self.actionMenu = createMenu(300, 480, self.width - 150,
    #                                  self.height - 240)
    #     self.actionLabel = text.Label("Action:",
    #                                   font_name="Arial",
    #                                   font_size=16,
    #                                   color=(255, 255, 255, 255),
    #                                   anchor_x="left",
    #                                   anchor_y="center")
    #     self.actionLabel.x = self.actionMenu.x - 120
    #     self.actionLabel.y = self.height - 30
    #     self.actionCell1 = None
    #     self.actionCell2 = None
