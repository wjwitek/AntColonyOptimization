from map import Map
import numpy as np


class Colony:
    def __init__(self, matrix: np.ndarray, alpha: float, iterations: int, intensity: int, ants_num: int,
                 evaporation: float):
        """
        Keeps all ants and a map and moves them in each iteration
        :param matrix: represents costs of moving between points
        :param alpha: importance of pheromone
        :param intensity: pheromone intensity
        :param ants_num: number of ants in colony
        :param evaporation: how quickly pheromone evaporates
        """
        self.start = 0
        self.map = Map(matrix)
        self.alpha = alpha
        self.iterations = iterations
        self.intensity = intensity
        self.ants_num = ants_num
        self.ants = None
        self.evaporation = evaporation

    def init_ants(self, ants_num):
        temp = []
        for i in range(ants_num):
            temp.append(Ant(self))
        return temp

    def update_pheromone(self):
        # evaporate pheromone
        for i in range(len(self.map.matrix)):
            for j in range(len(self.map.matrix)):
                if i == j:
                    continue
                self.map.pheromones[i][j] *= self.evaporation
        # add pheromones from ants
        for ant in self.ants:
            for i in range(1, len(ant.visited)):
                self.map.pheromones[ant.visited[i - 1]][ant.visited[i]] += self.intensity / self.map.matrix[ant.visited[i - 1]][ant.visited[i]]

    def solve_route(self):
        lowest_cost = float('inf')
        best_route = []
        for i in range(self.iterations):
            self.ants = self.init_ants(self.ants_num)
            for ant in self.ants:
                for _ in range(len(self.map.matrix) - 1):
                    ant.next_node()
                ant.travel_time += self.map.matrix[ant.visited[-1]][ant.visited[0]]
                ant.visited.append(ant.visited[0])
                if ant.travel_time < lowest_cost:
                    lowest_cost = ant.travel_time
                    best_route = ant.visited.copy()
                self.update_pheromone()
        return lowest_cost, best_route


class Ant:
    def __init__(self, colony: Colony):
        self.colony = colony
        self.current_position = colony.start
        self.visited = []
        self.visited.append(self.current_position)
        self.travel_time = 0
        self.prev_position = -1

    def next_node(self):
        # create list of possible next nodes
        possible_nodes = []
        for i in range(len(self.colony.map)):
            if i not in self.visited:
                possible_nodes.append(i)

        # calculate denominator
        den = 0
        for i in possible_nodes:
            den += self.colony.map.pheromones[self.current_position][i] ** self.colony.alpha

        # calculate probabilities for each next node
        probabilities = []
        for i in range(len(self.colony.map)):
            if i in possible_nodes:
                probabilities.append(self.colony.map.pheromones[self.current_position][i] ** self.colony.alpha / den)
        probabilities = np.asarray(probabilities)
        possible_nodes = np.asarray(possible_nodes)

        # select next node
        my_next_node = np.random.choice(a=possible_nodes, p=probabilities)
        self.prev_position = self.current_position
        self.visited.append(my_next_node)
        self.travel_time += self.colony.map.matrix[self.current_position][my_next_node]
        self.current_position = my_next_node

