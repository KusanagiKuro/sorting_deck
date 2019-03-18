#!/usr/bin/env python3

from pyglet import text
from utility import createMenu
from cell import Cell


class ActionMenu:
    def __init__(self, sortalgo, x, y):
        """
        Create an command menu

        Input: @x: float. The x coordinate
               @y: float. The y coordinate

        Note: Calculate from the center of the menu
        """
        # Set x, y to the correct value
        self.x = x - 200
        self.y = y - 240

        # Create the menu
        self.border = createMenu(400, 480, x - 200,
                                 y - 240)
        sortDict = {"bubble": "Bubble Sort Algorithm",
                    "insert": "Insert Sort Algorithm",
                    "quick": "Quick Sort Algorithm",
                    "merge": "Merge Sort Algorithm"
                    }
        # Create a label that describe the sort algorithm
        self.sortLabel = text.Label(sortDict[sortalgo],
                                    font_name="Arial",
                                    font_size=16,
                                    color=(255, 255, 255, 255),
                                    anchor_x="center",
                                    anchor_y="center",
                                    x=self.x,
                                    y=self.y + 220)
        # Create a constant command label
        self.commandLabel = text.Label("Action:",
                                       font_name="Arial",
                                       font_size=16,
                                       color=(255, 255, 255, 255),
                                       anchor_x="left",
                                       anchor_y="center",
                                       x=self.x - 180,
                                       y=self.y + 190)

        # Create cells that will be used to demonstrate the comparison
        self.cells = [Cell(None,
                           "",
                           self.x - 120,
                           self.commandLabel.y - 360,
                           15,
                           "",
                           "tealcircle.png"),
                      Cell(None,
                           "",
                           self.x + 120,
                           self.commandLabel.y - 360,
                           15,
                           "",
                           "tealcircle.png")]

        # Hide those cells so they don't get drawn
        for cell in self.cells:
            cell.setVisible(False)

        # Create a label that will display the current command
        self.commandText = text.Label("",
                                      font_name="Arial",
                                      font_size=16,
                                      bold=True,
                                      color=(255, 255, 255, 255),
                                      anchor_x="left",
                                      anchor_y="center",
                                      x=self.commandLabel.x + 80,
                                      y=self.commandLabel.y)

        # Create a condition label
        self.conditionLabel = text.Label("",
                                         font_name="Arial",
                                         font_size=12,
                                         color=(255, 255, 255, 255),
                                         anchor_x="left",
                                         anchor_y="center",
                                         x=self.commandLabel.x,
                                         y=self.commandLabel.y - 370)

        # Create a label that will display the condition of a Compare command
        self.conditionText = text.Label("",
                                        font_name="Arial",
                                        font_size=12,
                                        bold=True,
                                        color=(0, 255, 0, 255),
                                        anchor_x="left",
                                        anchor_y="center",
                                        x=self.conditionLabel.x + 100,
                                        y=self.conditionLabel.y)

        self.compareLabel = text.Label("Number of comparisons being made:",
                                       font_name="Arial",
                                       font_size=12,
                                       color=(255, 255, 255, 255),
                                       anchor_x="left",
                                       anchor_y="center",
                                       x=self.commandLabel.x,
                                       y=self.commandLabel.y - 400)

        self.compareText = text.Label("",
                                      font_name="Arial",
                                      font_size=12,
                                      color=(255, 255, 0, 255),
                                      anchor_x="left",
                                      anchor_y="center",
                                      x=self.commandLabel.x + 280,
                                      y=self.commandLabel.y - 400,
                                      bold=True)

        self.compareCount = 0

    def draw(self):
        """
        Draw the menu
        """
        # Border first
        self.border.draw()

        # Then all the labels
        self.sortLabel.draw()
        self.commandLabel.draw()
        self.commandText.draw()
        self.conditionLabel.draw()
        self.conditionText.draw()
        self.compareLabel.draw()
        self.compareText.draw()

        # Then the cells
        for cell in self.cells:
            cell.draw()

    def update(self):
        return [cell.update() for cell in self.cells]

    def executeCommand(self, command):
        """
        Changing the command menu based on the command

        Input: @command: a command.
        """
        # If the command is Exit, return
        if (command[0] == "Exit" or command[0] == "UpdateStatus" or
                command[0] == "CreateMarkers" or command[0] == "HideMarkers"):
            return

        # Dictionary contains the color corresponding to the command
        colorDict = {"Create": (0, 255, 0, 255),
                     "Swap": (143, 160, 255, 255),
                     "Compare": (255, 255, 0, 255),
                     "Result": (143, 160, 255, 255),
                     "Return": (143, 160, 255, 255),
                     "End Result": (0, 255, 0, 255),
                     "Shift": (213, 0, 213, 255),
                     "Split": (255, 255, 0, 255),
                     "MoveLeftMarker": (255, 255, 0, 255),
                     "MoveRightMarker": (255, 255, 0, 255)}

        # Dictionary contains the function corresponding to the command
        displayDict = {"Compare": self.displayCompareCommand,
                       "Result": self.displayResultCommand
                       }
        # Edit the command text base on the type of the command
        self.commandText.text = self.getCommandText(command)
        self.commandText.color = colorDict[command[0]]

        # Run the function according to the command
        displayDict.get(command[0], self.hideCompareCell)(command)

        self.compareText.text = str(self.compareCount)

    def displayResultCommand(self, command):
        """
        Display the result of the current comparing pair

        Input: @command: a Compare command.
        """
        # Dictionary contains value that needs to change based on the result
        # 1st is the vertical movement of 1st cell
        # 2nd is the vertical movement of 2nd cell
        # 3rd is the border of 1st cell
        # 4th is the border of 2nd cell
        valueDict = {"<": (-60, 60, "tealcircle.png", "resultborder.png"),
                     ">": (60, -60, "resultborder.png", "tealcircle.png"),
                     "=": (0, 0, "tealcircle.png", "tealcircle.png")}

        # Set the result key base on the result of the comparison
        result = ("<" if command[1][2] < command[1][3] else
                  ">" if command[1][2] > command[1][3] else
                  "=")

        # Apply the change on the cells.
        for index, cell in enumerate(self.cells):
            if valueDict[result][index]:
                cell.addTarget([(cell.x,
                                 cell.y + valueDict[result][index])])
            cell.setBorder(valueDict[result][index + 2])

    def displayCompareCommand(self, command):
        """
        Display the comparing pair of cells

        Input: @command: a Compare command.
        """
        # Set the value, visibility of each cell
        for index, cell in enumerate(self.cells):
            cell.setValue(command[1][-3 + index])
            cell.setIndex(command[1][index])
            cell.setPosition(self.x - 120 + index * 240,
                             self.commandLabel.y - 200)
            cell.setBorder("tealcircle.png")
            cell.setVisible(True)

        # Increase the total comparison that has been made by 1
        self.compareCount += 1

        # Display the condition that we are checking
        self.displayResultCommand(command)
        self.updateCondition(command)

    def hideCompareCell(self, command):
        """
        Hide the cell from being displayed.

        Input: @command: a command. Although it doesn't do anything here.
        """
        # Hide the cells.
        for cell in self.cells:
            cell.setVisible(False)

        # Hide the condition label.
        self.conditionText.text = ""
        self.conditionLabel.text = ""
        self.updateCondition(command)

    def updateCondition(self, command):
        # If the command isn't compare, hide the text and the label.
        if command[0] != "Compare":
            self.conditionText.text = ""
            self.conditionLabel.text = ""

        # Else, show them and update the condition
        else:
            self.conditionText.text = command[1][-1]
            self.conditionLabel.text = "Condition:"

    def getCommandText(self, command):
        """
        Return a formatted text that describe the command.

        Input: @command: a command.
        """
        if command[0] == "Compare":
            return " ".join([command[0], "lst[%d]" % command[1][0], "with",
                             "lst[%d]" % command[1][1]])

        elif command[0] == "Swap":
            return " ".join([command[0], "lst[%d]" % command[1][0], "with",
                             "lst[%d]" % command[1][1]])

        elif command[0] == "Shift":
            return " ".join([command[0], "lst[%d]" % command[1][0],
                             "to index", str(command[1][1])])

        elif command[0] == "Split":
            return " ".join([command[0],
                             "lst[%d:%d]" % (command[1][0],
                                             command[1][2]),
                             "at index %d" % command[1][1]])
        elif command[0] == "MoveLeftMarker":
            return " ".join(["Move Left Marker to",
                             "lst[%d]" % command[1][-1]])
        elif command[0] == "MoveRightMarker":
            return " ".join(["Move Right Marker to",
                             "lst[%d]" % command[1][-1]])
        else:
            return command[0]
