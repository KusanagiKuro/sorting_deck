#!usr#!/usr/bin/env python3
import os
import pyglet
from math import floor
from pyglet import text, image, resource, sprite
from pyglet.window import Window, key
from utility import *
from cell import *
from celllist import *


class Model:
    def __init__(self, lst):
        self.window = pyglet.window.Window(resizable=False,
                                           caption="Visualisator",
                                           fullscreen=True)
        background = resource.image("background.png")
        self.background = sprite.Sprite(background)
        self.background.scale_x = self.window.width / background.width
        self.background.scale_y = self.window.height / background.height
        self.initialList = CellList(lst, self.window.width // 2,
                                    self.window.height - 72)

    def draw(self):
        self.window.clear()
        self.background.draw()
        self.initialList.draw()

    def update(self, dt):
        self.initialList.update(dt)
