#!/usr/bin/env python3
import sys

texture = resource.texture("square.png")
texture.anchor_x = texture.width // 2
texture.anchor_y = texture.height // 2
self.window = pyglet.window.Window(1280, 720, visible=False,
                                   resizable=False,
                                   style=Window.WINDOW_STYLE_DIALOG,
                                   caption="Visualisator")
