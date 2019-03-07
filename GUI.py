#!/usr/bin/env python3
import os
import pyglet
from math import floor
from pyglet import text, image, resource, sprite
from pyglet.window import Window, key
from utility import *
from model import *
from cell import *
from celllist import *


def swap(cell1, cell2):
    cell1.targetList.append((cell2.x, cell2.y),
                            (cell2.x, cell2.y + 72)
                            (cell1.x, cell2.y + 72))
    cell2.targetList.append((cell1.x, cell1.y),
                            (cell1.x, cell1.y - 72)
                            (cell2.x, cell1.y - 72))


def GUI():
    resource.path = ['res']
    resource.reindex()
    pyglet.gl.glClearColor(0.5, 0, 0, 1)
    arr = [1, 2, 3, 43, 544, 6555, 76666, 12312222, 9, 10, 11, 12, 13, 14,
           12]
    myModel = Model(arr)

    @myModel.window.event
    def on_draw():
        myModel.draw()

    @myModel.window.event
    def on_key_press(symbol, modifier):
        if symbol == key.UP:
            myModel.initialList.vectorY += 1
        elif symbol == key.DOWN:
            myModel.initialList.vectorY -= 1
        elif symbol == key.RIGHT:
            myModel.initialList.vectorX += 1
        elif symbol == key.LEFT:
            myModel.initialList.vectorX -= 1

    @myModel.window.event
    def on_key_release(symbol, modifier):
        if symbol == key.UP:
            myModel.initialList.vectorY -= 1
        elif symbol == key.DOWN:
            myModel.initialList.vectorY += 1
        elif symbol == key.RIGHT:
            myModel.initialList.vectorX -= 1
        elif symbol == key.LEFT:
            myModel.initialList.vectorX += 1

    pyglet.clock.schedule_interval(myModel.update, 1/120.0)
    pyglet.app.run()


if __name__ == "__main__":
    GUI()
