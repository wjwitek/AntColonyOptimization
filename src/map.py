import numpy as np


class Map:
    def __init__(self, matrix: np.ndarray):
        """
        Represents routes in travelling salesman problem.
        :param matrix: costs of travelling between points
        """
        self.matrix = matrix
        self.pheromones = np.zeros(shape=matrix.shape)
        for i in range(len(self)):
            for j in range(len(self)):
                if i == j:
                    self.pheromones[i][j] = float('inf')
                else:
                    self.pheromones[i][j] = 1 / (len(self) * len(self))
        self.heuristic = np.zeros(shape=matrix.shape)
        for i in range(len(self)):
            for j in range(len(self)):
                if i == j:
                    self.heuristic[i][j] = float('inf')
                else:
                    self.heuristic[i][j] = 1 / len(self)

    def __len__(self):
        return len(self.matrix)
