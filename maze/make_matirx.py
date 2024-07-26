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

    def repeated_point(self, point):
        if self.maze[point] == 0:
            return True
        return False

    def make_random_maze(self):
        self.maze[self.start_point[0], self.start_point[1]] = 0
        self.maze[self.end_point[0], self.end_point[1]] = 0
        self.queue.append(self.start_point)
        counter = 0
        past_point = (0, 0)
        while self.queue:
            point = self.queue.popleft()
            if self.is_valid_point(point) and not self.is_frontier(point) and not self.is_block(point):
                self.set_maze_cell(point)
            if not self.is_block(point):
                self.next_points = self.next_move(point)
            elif self.is_block(point):
                saver_point = point
                point = past_point
                self.next_points = self.next_move(point)
                if saver_point in self.next_points:
                    self.next_points.remove(saver_point)
            if self.next_points:
                walk_point_number = random.randint(0, len(self.next_points) - 1)
                if walk_point_number == 0:
                    selected_points = random.choices(self.next_points, k=1)
                else:
                    selected_points = random.choices(self.next_points, k=walk_point_number)
                self.add_to_queue(selected_points)
            counter += 1
            past_point = point
            if point == self.end_point:
                return True


    def draw_maze(self):
        plt.figure(figsize=(10, 10))
        plt.imshow(self.maze, cmap='binary')
        plt.title('100x100 Maze with Surrounding Walls, Start, and End Points')
        plt.axis('off')
        plt.show()


maze = MakeMaze(20, (0, 1), (18, 19))
maze.make_random_maze()
maze.draw_maze()
