# AStar
A* is a pathfinding algorithm that uses heuristics to find the shortest path from a start to a goal. 
This project implements various versions of A* from scratch to help a computer agent solve a previously unseen maze. 

## Using the code 

### Relevant Files
#### 1. Maze.py
##### generate_actual_maze(self, size):
Generates a random maze of inputted size, where on average 30% of cells are blocked and 70% are unblocked. 
##### generate_blank_maze(self, size):
A blank maze is generated where all cells are marked as open. This maze represents the computer agent's initial knowledge of the actual maze.
#### 2. RepeatedAlgo.py
RepeatedAlgo.py not only finds the quickest path, using SolveMaze.py, on the agent's map, but then tests this path on the actual maze. If an obstacle is found on the actual maze using the calculated path, the agent moves to the obstacle, marks this obstacle on it's own maze, and then recalculates another path (on SolveMaze.py) using it's newly improved map. 
#### 3. SolveMaze.py
This code contains two types of A* algorithms on which users can run the code (for more details, scroll down to Finding the quickest path).
#### 4. Metrics.py 
A bunch of helper functions
#### 5. Visual.py
Creates the visuals to show how the agent solves the maze.
#### 6. UserInterface.py
Takes user inputs through the terminal to run the project. Users can:
- Change maze size (defaulted to 25x25, the optimal size)
  - This generates a random maze of size nxn, where n is inputted by the user
  - Call this command to run the A* algorithms on a different maze as well. 
- Run forward A*
- Run adaptive A*

### Installation and Running
- Download as zip
- Unzip file
- Open file in your preferred source code editor that supports Python 
- Run UserInterface.py
- Follow the commands in the terminal window to see results 

#### Dependencies
Tkinter

### Understanding the visuals
- Gray squares are discovered blocked cells.
- Black squares are blocked cells discovered with the last A* pathfinding. 
- Black square with a green circle is the goal cell.
- Black square with a red circle is the start cell.
- Circles with the blue outline represent cells in the open list
- Filled in circled are cells in the closed list. Cells closer in color to red are farther from the goal, likewise cells closer in color to green are closer to the goal.

![Alt Text](https://media.giphy.com/media/RfqMyeRszPyRMPB0PG/giphy.gif)

## A Deeper Understanding
### Generating a maze:
The maze is generated by a depth first search through the maze and traversing each cells neighbor randomly. Before every cell is entered into the open list, we generate a random integer from 1-100. If the integer is greater than 70, the cell is marked as block by making its cost infinity, otherwise the cost is kept as 1. Each cell has an associated cost. 

### Finding the shortest path
A* is a modification on breadth/depth first search where cells with the lowest f-values are visited first. Each cell has an f-value associated with it. A cell's f-value is the sum of it's distance from start and distance to goal. This means that cells that give the shortest path are visited first, therefore A* will tend to return a shortest path from the start to goal.
```
f = g+h = distance from start to current cell + estimated distance from current cell to goal
g = sum of the cell costs from start to current cell
h = estimated distance from current cell to goal
```

#### forward_A_star(self, start_node,  goal_node, w):
Forward A* calculates f values as follows:
```
f = g+h = distance from start to current + estimated distance from current to goal
g = sum of cell costs from start to current cell
h = | cell.x - goal.x | + | cell.y - goal.y | = Manhattan distance
f in effect estimates the path's length, assuming no obstacles exist between the current cell and goal
```
Manhattan distance is a type of heuristic. Heuristics are used to make a more informed decision about which cells to expand first so that we reach the goal as soon as possible. Compare A* to DFS/BFS, where cells are expanded without thought to which cell will help us reach the goal first. 

#### adaptive_A_star(self, start_node, goal_node, lastClosedList, w):
A modification on forward A* where cells where f-values are the sum of the distance from start to current cell and distance to goal (calculated as previous search's distance from start to goal minus distance from start to current cell). 
```
f = g+h = distance from start to current + estimated distance from current to goal
g = sum of cell costs from start to current cell
For cell's first being encountered: 
h = | cell.x - goal.x | + | cell.y - goal.y | = Manhattan distance 
For cell's encountered in previous searches: 
h = (last search's path length) - g
f in effect estimates the path's length, taking into account any obstacle's encountered in the previous searches
```

###
For a more detailed explanation and analysis of this project click [here](AStar.pdf). 

## Author
Bharti Mehta
