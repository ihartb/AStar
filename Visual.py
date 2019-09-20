from colour import Color
from tkinter import *


class Visual:
    def __init__(self, start, goal, size):
        self.master = Tk()
        self.size = size
        self.distance = 550 // self.size
        self.canSize = self.distance*(self.size + 2)
        self.canvas = Canvas(self.master, width=self.canSize, height=self.canSize)
        self.canvas.pack()
        self.colors = list(Color("#00FF00").range_to(Color("#FF0000"), 100))
        self.startNode = start
        self.goalNode = goal


    def pixelLocation(self, x0, y0):
        x = y0 * self.distance
        y = x0 * self.distance
        x1 = x + self.distance
        y1 = y + self.distance
        x2 = x1 + self.distance
        y2 = y1 + self.distance

        return x1, y1, x2, y2

    def showMaze(self, maze):
        for x in range(0, self.size):
            for y in range(0, self.size):
                cell = maze[x][y]
                x1, y1, x2, y2 = self.pixelLocation(x, y)
                if cell.cost != 1:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="#E8E8E8", outline="#E8E8E8")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="#FFFFFF", outline="#FFFFFF")
        self.start()
        self.goal()
        self.master.update()

    def blocked(self, cell):
        x1, y1, x2, y2 = self.pixelLocation(cell.x, cell.y)

        if cell.cost != 1:
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="#000000", outline="#000000")

    def start(self):
        x1, y1, x2, y2 = self.pixelLocation(self.startNode.x, self.startNode.y)
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="#000000", outline="#000000")
        self.canvas.create_oval(x1+2,y1+2,x2-2,y2-2, fill='#FF0000', outline='#FF0000')


    def goal(self):
        x1, y1, x2, y2 = self.pixelLocation(self.goalNode.x, self.goalNode.y)
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="#000000", outline="#000000")
        self.canvas.create_oval(x1+2,y1+2,x2-2,y2-2, fill='#00FF00', outline='#00FF00')

    def inOpen(self, cell):
        if (cell == self.startNode) or (cell == self.goalNode): return
        x1, y1, x2, y2 = self.pixelLocation(cell.x, cell.y)

        self.canvas.create_rectangle(x1, y1, x2, y2, fill="#FFFFFF", outline="#FFFFFF")
        self.canvas.create_oval(x1+2, y1+2, x2-2, y2-2, fill='white', outline='blue')
        self.master.update()

    def inClosed(self, cell):
        if (cell == self.startNode) or (cell == self.goalNode): return
        cellH = abs(cell.x - self.goalNode.x) + abs(cell.y - self.goalNode.y)
        startH = abs(self.startNode.x - self.goalNode.x) + abs(self.startNode.y - self.goalNode.y)

        percent = cellH/startH
        index = int(percent * 99)
        while (index > 99):
            percent = cell.g / self.goalNode.g
            index = 99-int(percent * 99)
        current = self.colors[index]

        x1, y1, x2, y2 = self.pixelLocation(cell.x, cell.y)
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="#FFFFFF", outline="#FFFFFF")
        self.canvas.create_oval(x1+2, y1+2, x2-2, y2-2, fill=current, outline=current)
        self.master.update()

    def pathLine(self, steps):
        parent1 = steps.pop(0)
        parent = parent1
        for current in steps:
            x1, y1, x2, y2 = self.pixelLocation(parent.x, parent.y)
            x1 = (x1 + x2) // 2
            y1 = (y1 + y2) // 2

            x2, y2, x3, y3 = self.pixelLocation(current.x, current.y)
            x2 = (x2 + x3) // 2
            y2 = (y2 + y3) // 2
            self.canvas.create_line(x1, y1, x2, y2, fill='purple', width=3)
            parent = current
            self.master.update()
        steps.insert(0, parent1)

    def finalPath(self, maze, path):
        self.showMaze(maze)
        self.pathLine(path)

    def noPath(self):
        self.canvas.create_text( self.size*self.distance//2, self.size*self.distance//2, text="Path not found")
        self.master.update()
