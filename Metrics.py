import random
from Visual import Visual


class Metrics:
    def traverse_path(self, goal_node, start_node):
        path = [goal_node]
        currentNode = goal_node
        while currentNode is not start_node:
            currentNode = currentNode.parent
            path.append(currentNode)
        path.reverse()
        return path

    def generate_random_start_and_goal_nodes(self, actual_maze, size):
        while True:
            start_node_actual = actual_maze[random.randint(0, size-1)][random.randint(0, size-1)]
            goal_node_actual = actual_maze[random.randint(0, size-1)][random.randint(0, size-1)]
            if (start_node_actual.cost == 1) & (goal_node_actual.cost == 1) & (start_node_actual != goal_node_actual):
                break
        return start_node_actual, goal_node_actual

    def blockage_status_of_children(self, start_node, start_node_actual, w):
        for i in range(0,4):
            child_actual = start_node_actual.traverse_children(i)
            if child_actual is not None:
                child = start_node.traverse_children(i)
                child.cost = child_actual.cost
                w.blocked(child)
        w.master.update()
        w.master.after(200)

    def initializeVisuals(self, start_node, goal_node, size, actual_maze, agent_maze):
        w = Visual(start_node, goal_node, size)
        w.showMaze(actual_maze)
        w.showMaze(agent_maze)
        return w
