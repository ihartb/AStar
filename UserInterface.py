from Maze import Maze
from RepeatedAlgo import RepeatedAlgo
from Metrics import Metrics
from Visual import Visual


class UserInterface:

    def __init__(self):
        self.maze = Maze()
        self.metrics = Metrics()

        self.size = 25
        self.actual_maze = self.maze.generate_actual_maze(self.size)
        self.start_node_actual, self.goal_node_actual = self.metrics.generate_random_start_and_goal_nodes(
                    self.actual_maze, self.size)

    def user(self):
        user_input = None
        print("0: Choose maze size, nxn\n"
              "1: Perform Repeated forward A*\n"
              "2: Perform Repeated Adaptive A*\n"
              "q: Quit\n")

        while user_input != "q":

            user_input = input("Choose one of the numbers above : ")

            if user_input == "0":
                self.size = int(input("Enter the size of the maze, n: "))
                self.actual_maze = self.maze.generate_actual_maze(self.size)
                self.start_node_actual, self.goal_node_actual = Metrics().generate_random_start_and_goal_nodes(
                    self.actual_maze, self.size)

            elif user_input == "1":
                RepeatedAlgo(self.size, self.actual_maze, self.start_node_actual,
                             self.goal_node_actual, 1).repeated_algorithm()

            elif user_input == "2":
                RepeatedAlgo(self.size, self.actual_maze, self.start_node_actual,
                             self.goal_node_actual, 2).repeated_algorithm()

UserInterface().user()
