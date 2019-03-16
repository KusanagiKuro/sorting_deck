#!/usr/bin/env python3
import pyglet
from pyglet import resource
from window import *


def GUI(commandList):
    "Starting a visualisator that runs on the commandList"
    for item in commandList:
        print(item)

    # Setup the resource directory for pyglet
    resource.path = ['res']
    resource.reindex()
    pyglet.gl.glClearColor(0.5, 0, 0, 1)

    # Create the visualisator window
    window = Window(commandList, resizable=False,
                    caption="Visualisator",
                    fullscreen=True)

    # Let the app run with the window update function runs 120 times/second
    pyglet.clock.schedule_interval(window.update, 1/120.0)

    # Let the game begin
    pyglet.app.run()
