from SolveMaze import SolveMaze
from Metrics import Metrics
from Maze import Maze

class RepeatedAlgo:
    def __init__(self, size, actual_maze, start_node_actual, goal_node_actual, algo_type):
        self.size = size
        self.actual_maze = actual_maze
        self.start_node_actual = start_node_actual
        self.goal_node_actual = goal_node_actual
        self.algo_type = algo_type

        self.agent_maze = Maze().generate_blank_maze(self.size)
        self.start_node = self.agent_maze[self.start_node_actual.x][self.start_node_actual.y]
        self.goal_node = self.agent_maze[self.goal_node_actual.x][self.goal_node_actual.y]

        self.solvedMaze = []
        self.w = Metrics().initializeVisuals(self.start_node, self.goal_node, self.size, self.actual_maze, self.agent_maze)



    def repeated_algorithm(self):
        start_node = self.start_node

        Metrics().blockage_status_of_children(start_node, self.start_node_actual, self.w)

        self.goal_node.update_g(float("inf"))
        lastClosedList = set()

        while start_node is not self.goal_node:
            self.w.showMaze(self.agent_maze)
            passed = 0
            if self.algo_type == 1:
                passed = SolveMaze().forward_A_star(start_node, self.goal_node, self.agent_maze, self.w)
            elif self.algo_type == 2:
                passed = SolveMaze().adaptive_A_star(start_node, self.goal_node, lastClosedList, self.w)

            if passed == 0:
                print("I can't reach the target")
                self.w.noPath()
                break

            path = Metrics().traverse_path(self.goal_node, start_node)
            self.w.pathLine(path)

            for i in path:
                if i.cost == self.actual_maze[i.x][i.y].cost:
                    if i in self.solvedMaze:
                        del self.solvedMaze[self.solvedMaze.index(i) + 1: len(self.solvedMaze)]
                        continue
                    self.solvedMaze.append(i)
                else:
                    start_node = self.solvedMaze.pop()
                    start_node_actual = self.actual_maze[start_node.x][start_node.y]
                    Metrics().blockage_status_of_children(start_node, start_node_actual, self.w)
                    break

            if self.solvedMaze[-1] == self.goal_node:
                print("I reached the goal")
                self.w.finalPath(self.actual_maze, self.solvedMaze)
                break

