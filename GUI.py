#!/usr/bin/env python3
import os
import pyglet
from math import floor
from pyglet import text, image, resource, sprite
from pyglet.window import Window, key
from utility import *
from mywindow import *
from cell import *
from celllist import *


def cellSwap(cell1, cell2):
    cell1.targetList.append((cell2.x, cell2.y),
                            (cell2.x, cell2.y + 80)
                            (cell1.x, cell2.y + 80))
    cell2.targetList.append((cell1.x, cell1.y),
                            (cell1.x, cell1.y - 80)
                            (cell2.x, cell1.y - 80))


def GUI(commandList):
    "Starting a visualisator that runs on the commandList"
    resource.path = ['res']
    resource.reindex()
    pyglet.gl.glClearColor(0.5, 0, 0, 1)
    print(commandList)
    window = MyWindow(commandList, resizable=False,
                      caption="Visualisator",
                      fullscreen=True)

    pyglet.clock.schedule_interval(window.update, 1/120.0)
    pyglet.app.run()
