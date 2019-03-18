#!/usr/bin/env python3


def GUI(sortalgo, commandList, sortalgo2, commandList2):
    """
    Starting a visualisator that runs on the commandList

    Input: @sorttype: string. Type of the sort
           @commandList: list of commands.
    """
    import pyglet
    from pyglet import resource
    from window import Window

    # Setup the resource directory for pyglet
    resource.path = ['res']
    resource.reindex()
    for command in commandList2:
        print(command)

    # Create the visualisator window
    window = Window(sortalgo, commandList, sortalgo2, commandList2,
                    resizable=False,
                    caption="Visualisator",
                    fullscreen=True)

    # Let the app run with the window update function runs 120 times/second
    pyglet.clock.schedule_interval(window.update, 1/120)

    # Let the game begin
    pyglet.app.run()
