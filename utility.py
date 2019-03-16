#!/usr/bin/env python3
from pyglet import sprite, resource


def swapValueInList(lst, index1, index2, commandList):
    """
    Swap value between two elements of a lst if the first is higher
    """
    makeCommand(commandList, "Swap", index2, index2 + 1)
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return True


def createSprite(path="circle.png"):
    """
    Create a sprite by using the image in the path and recenter it

    Input: @path: string. The path to the image
    """
    # Get the texture from the path
    texture = resource.texture(path)

    # Recenter the anchor point
    texture.anchor_x = texture.width // 2
    texture.anchor_y = texture.height // 2

    # Return the sprite made from the texture
    return sprite.Sprite(texture)


def createCellBorder(path="circle.png"):
    """
    Create the border for a cell
    """
    # Get the border from the createBorder function
    border = createSprite(path)

    # Resize it to the wanted size and return it.
    border.scale = 96 / 1265 * 1.4
    return border


def createMenu(width, height, x, y):
    """
    Create a menu with width and height at position x, y

    Input: @width: float. The width of the menu
           @height: float. The height of the menu
           @x: integer. The coordinate x
           @y: integer. The coordinate y
    """
    # Create the menu border and background
    menu = createSprite("rectangle.png")

    # Resize it to the wanted size
    menu.scale_x = width / 200
    menu.scale_y = height / 400

    # Set its position
    menu.x = x
    menu.y = y

    # Set its transparency
    menu.opacity = 125
    return menu
