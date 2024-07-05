from maze.maze_structure import MazeStructure
from maze.stack import Stack


class Maze:
    def __init__(self):
        pass

    def solve(self):
        stack = Stack()
        maze = MazeStructure().structure()
        row = 1
        col = 5
        maze[1,5] = 2
        is_continue = True
        current_position = ()
        while current_position != (12,19):
            if maze[row + 1, col] == 0:
                if not (row + 1, col) in stack.stack:
                    stack.push((row + 1, col))
                    is_continue = False
            if maze[row, col + 1] == 0:
                if is_continue:
                    if not (row, col + 1) in stack.stack:
                        stack.push((row, col + 1))
                        is_continue = False
            if maze[row, col - 1] == 0:
                if is_continue:
                    if not (row, col - 1) in stack.stack:
                        stack.push((row, col - 1))
                        is_continue = False
            if maze[row - 1, col] == 0:
                if is_continue:
                    if not (row - 1, col) in stack.stack:
                        stack.push((row - 1, col))
                        is_continue = False
            if is_continue:
                if current_position in stack.stack[0:stack.top_index+1]:
                    for i in range(stack.top_index):
                        maze[stack.top()[0], stack.top()[1]] = 2
                        stack.remove()

            is_continue = True
            row = stack.top()[0]
            col = stack.top()[1]
            current_position = (row,col)

        print("maze solved")

        for i in range(len(stack.stack)):
            maze[stack.stack[i][0],stack.stack[i][1]] = 3
        print(maze)


myMaze = Maze()
myMaze.solve()