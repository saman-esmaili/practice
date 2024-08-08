import numpy as np
import random
import matplotlib.pyplot as plt
from collections import deque


class MakeMaze:
    def __init__(self, N, start_point, end_point):
        self.N = N
        self.start_point = start_point
        self.end_point = end_point
        self.maze = np.ones((self.N, self.N), dtype=int)
        self.queue = deque()

    def is_frontier(self, point):
        if point[0] == 0 or point[0] == self.N - 1 or point[1] == 0 or point[1] == self.N - 1:
            return True
        return False

    def is_valid_point(self, point):
        i = point[0]
        j = point[1]
        if 0 <= point[0] < self.N and 0 <= point[1] < self.N and self.maze[i, j] != 0:
            return True
        return False

    def next_move(self, current_point):
        next_points = []
        left_point = (current_point[0], current_point[1] - 1)
        right_point = (current_point[0], current_point[1] + 1)
        top_point = (current_point[0] - 1, current_point[1])
        bottom_point = (current_point[0] + 1, current_point[1])
        if self.is_valid_point(left_point) and not self.is_frontier(left_point):
            next_points.append(left_point)
        if self.is_valid_point(right_point) and not self.is_frontier(right_point):
            next_points.append(right_point)
        if self.is_valid_point(top_point) and not self.is_frontier(top_point):
            next_points.append(top_point)
        if self.is_valid_point(bottom_point) and not self.is_frontier(bottom_point):
            next_points.append(bottom_point)
        return next_points

    def add_to_queue(self, points):
        for point in points:
            self.queue.append(point)

    def set_maze_cell(self, point):
        self.maze[point[0]][point[1]] = 0

    def is_block(self, point):
        left = (point[0], point[1] - 1)
        bottom = (point[0] + 1, point[1])
        left_bottom = (point[0] + 1, point[1] - 1)
        top = (point[0] - 1, point[1])
        right = (point[0], point[1] + 1)
        top_right = (point[0] - 1, point[1] + 1)
        top_left = (point[0] - 1, point[1] - 1)
        right_bottom = (point[0] + 1, point[1] + 1)
        if self.maze[left] == 0 and self.maze[bottom] == 0 and self.maze[left_bottom] == 0:
            return True
        elif self.maze[top] == 0 and self.maze[right] == 0 and self.maze[top_right] == 0:
            return True
        elif self.maze[left] == 0 and self.maze[top_left] == 0 and self.maze[top] == 0:
            return True
        elif self.maze[right] == 0 and self.maze[right_bottom] == 0 and self.maze[bottom] == 0:
            return True
        return False
    def make_random_maze(self):
        self.maze[self.start_point[0], self.start_point[1]] = 0
        self.maze[self.end_point[0], self.end_point[1]] = 0
        self.queue.append(self.start_point)
        counter = 0
        past_point = (0, 0)
        past = (0,0)
        self.lst = []
        while self.queue:
            point = self.queue.popleft()
            self.lst.append(point)
            if past_point < point:
                past_point = point
            if self.is_valid_point(point) and not self.is_frontier(point) and not self.is_block(point):
                self.set_maze_cell(point)
            if not self.is_block(point):
                self.next_points = self.next_move(point)
            elif self.is_block(point) or self.is_frontier(point):
                if self.lst[len(self.lst)-1] == self.lst[len(self.lst)-2] and self.lst[len(self.lst)-2] == self.lst[len(self.lst)-3] and self.lst[len(self.lst)-3] == self.lst[len(self.lst)-4]:
                    point = past_point
                else:
                    point = past
                self.next_points = self.next_move(point)

            if self.next_points:
                selected_points = random.choices(self.next_points)
                self.add_to_queue(selected_points)
            counter += 1
            if counter % 80 == 0:
                self.draw_maze()
            past = point
            if self.maze[self.end_point[0]-1,self.end_point[1]] == 0 or self.maze[self.end_point[0],self.end_point[1]-1] == 0:
                return True
    def draw_maze(self):
        plt.figure(figsize=(10, 10))
        plt.imshow(self.maze, cmap='binary')
        plt.title('100x100 Maze with Surrounding Walls, Start, and End Points')
        plt.axis('off')
        plt.show()


maze = MakeMaze(20, (0, 1), (18, 19))
print(maze.make_random_maze())
maze.draw_maze()
