import numpy as np

class Fibonacci:
    def __init__(self):
        self.number = int(input("enter number:"))
        self.solution()

    def solution(self):
        matrix = np.ones(self.number)
        for col in range(2,matrix.shape[0]):
          matrix[col] = matrix[col-1] + matrix[col-2]
        print(matrix)

Fibonacci()