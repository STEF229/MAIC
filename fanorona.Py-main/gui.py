from tkinter.constants import Y
from graphics import *


class GUI:
    buttons = list()
    window = GraphWin()

    def __init__(self, window) -> None:
        self.window = window

    def addButton(self, button):
        self.buttons.append(button)

    def Draw(self):
        for button in self.buttons:
            button.Draw(self.window)


class Button:
    point = Point(0, 0)
    point2 = Point(10, 10)

    def __init__(self, x, y, x1, y1) -> None:
        self.point = Point(x, y)

    def Draw(self, win):
        Rectangle(self.point, self.point2).draw(win)
