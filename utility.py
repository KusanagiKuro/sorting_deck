#!/usr/bin/env python3
from pyglet import resource, sprite


def swapValue(object1, object2):
    """
    Swap value between two elements of a lst if the first is higher
    """
    object1, object2 = object2, object1
    return True


def makeCommand(name, *args):
    return (name, args)


def createBorder(path="circle.png"):
    texture = resource.texture(path)
    texture.anchor_x = texture.width // 2
    texture.anchor_y = texture.height // 2
    return sprite.Sprite(texture)


def createMenu(size_x, size_y, x, y):
    menu = createBorder("rectangle.png")
    menu.scale_x = size_x / 200
    menu.scale_y = size_y / 400
    menu.x = x
    menu.y = y
    menu.opacity = 125
    return menu
