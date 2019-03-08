#!/usr/bin/env python3
from pyglet import resource, sprite


def swap(lst, first, second):
    """
    Swap value between two elements of a lst if the first is higher
    """
    lst[first], lst[second] = lst[second], lst[first]
    return True


def makeCommand(*args):
    return (args[0], [arg for arg in args[1:]])


def createBorder(path="circle.png"):
    texture = resource.texture(path)
    texture.anchor_x = texture.width // 2
    texture.anchor_y = texture.height // 2
    return sprite.Sprite(texture)
