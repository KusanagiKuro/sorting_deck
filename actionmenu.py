#!/usr/bin/env python3

from pyglet import text
from utility import createMenu
from cell import *


class ActionMenu():
    def __init__(self, x, y):
        self.x = x - 200
        self.y = y - 240
        self.border = createMenu(400, 480, x - 200,
                                 y - 240)
        self.commandLabel = text.Label("Action:",
                                       font_name="Arial",
                                       font_size=16,
                                       color=(255, 255, 255, 255),
                                       anchor_x="left",
                                       anchor_y="center",
                                       x=self.x - 180,
                                       y=self.y + 220)
        self.resultLabel = text.Label("Result:",
                                      font_name="Arial",
                                      font_size=16,
                                      color=(255, 255, 255, 255),
                                      anchor_x="left",
                                      anchor_y="center",
                                      x=self.x - 180,
                                      y=self.y - 200)
        self.compareCell1 = None
        self.compareCell2 = None
        self.commandText = text.Label("",
                                      font_name="Arial",
                                      font_size=16,
                                      bold=True,
                                      color=(255, 255, 255, 255),
                                      anchor_x="left",
                                      anchor_y="center",
                                      x=self.commandLabel.x + 100,
                                      y=self.commandLabel.y)
        self.resultText = text.Label("",
                                     font_name="Arial",
                                     font_size=16,
                                     bold=True,
                                     color=(255, 255, 255, 255),
                                     anchor_x="left",
                                     anchor_y="center",
                                     x=self.resultLabel.x + 100,
                                     y=self.resultLabel.y)

    def draw(self):
        self.border.draw()
        self.commandLabel.draw()
        self.resultLabel.draw()
        self.commandText.draw()
        self.resultText.draw()
        try:
            self.compareCell1.draw()
            self.compareCell2.draw()
        except AttributeError:
            pass

    def updateCommand(self, command):
        colorDict = {"Create": (0, 255, 0, 255),
                     "Lock": (255, 0, 0, 255),
                     "Swap": (143, 160, 255, 255),
                     "Compare": (255, 255, 0, 255),
                     "Result": (143, 160, 255, 255)}
        displayDict = {"Create": self.display,
                       "Lock": self.display,
                       "Swap": self.display,
                       "Compare": self.displayCompare,
                       "Result": self.displayResult
                       }
        self.commandText.text = command[0]
        self.commandText.color = colorDict[command[0]]
        if command[0] != "Result":
            self.resultText.visible = False
        displayDict[command[0]](command)

    def displayResult(self, command):
        self.resultText.visible = True
        self.resultText.text = (self.compareCell1.getValue() +
                                " is " + command[1][-1] + " " +
                                self.compareCell2.getValue())
        if "less" in command[1][-1]:
            self.compareCell1.addTarget([(self.compareCell1.x,
                                          self.compareCell1.y - 60)])
            self.compareCell2.addTarget([(self.compareCell2.x,
                                          self.compareCell2.y + 60)])
        pyglet.clock.schedule_interval(self.compareCell1.update, 1/60)
        pyglet.clock.schedule_interval(self.compareCell2.update, 1/60)

    def displayCompare(self, command):
        self.compareCell1 = Cell(command[1][-2],
                                 self.x - 120,
                                 self.resultLabel.y + 200,
                                 15,
                                 -1,
                                 "comparecircle.png")
        self.compareCell2 = Cell(command[1][-1],
                                 self.x + 120,
                                 self.resultLabel.y + 200,
                                 15,
                                 -1,
                                 "comparecircle.png")
        self.compareCell1.draw()
        self.compareCell2.draw()

    def display(self, *args):
        pass
