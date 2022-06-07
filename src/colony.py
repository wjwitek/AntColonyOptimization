from map import Map
from typing import List, Tuple
import numpy as np


class Colony:
    def __init__(self, matrix: np.ndarray, alpha: float, iterations: int, intensity: int, ants_num: int,
                 evaporation: float, beta: float):
        """
        Keeps all ants and a map and moves them in each iteration
        :param matrix: represents costs of moving between points
        :param alpha: importance of pheromone in choosing route
        :param intensity: pheromone intensity (how much ants deposit)
        :param ants_num: number of ants in colony
        :param evaporation: how quickly pheromone evaporates
        :param beta: how much heuristic is important
        """
        self.start = 0
        self.map = Map(matrix)
        self.alpha = alpha
        self.iterations = iterations
        self.intensity = intensity
        self.ants_num = ants_num
        self.ants = None
        self.evaporation = evaporation
        self.beta = beta

    def init_ants(self, ants_num) -> List:
        """
        Create set of new ants
        :param ants_num: number of ants
        :return: list of ants
        """
        temp = []
        for i in range(ants_num):
            temp.append(Ant(self))
        return temp

    def update_pheromone(self):
        """
        Reduces present pheromone according to evaporation rate, and then adds pheromones deposited by ants.
        """
        # evaporate pheromone
        for i in range(len(self.map.matrix)):
            for j in range(len(self.map.matrix)):
                if i == j:
                    continue
                self.map.pheromones[i][j] *= self.evaporation
        # add pheromones from ants
        for ant in self.ants:
            for i in range(1, len(ant.visited)):
                # divide by length of whole road to make longer routes less desirable
                self.map.pheromones[ant.visited[i - 1]][ant.visited[i]] += self.intensity / ant.travel_time

    def solve_route(self) -> Tuple[int, List[int]]:
        """
        Looks for best solution. For each iteration creates new set of ants, each of them choose route and then
        pheromones are updated.
        :return: lowest found time of travel and corresponding route
        """
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
        """
        Single ant that travels through map.
        :param colony: ant's colony
        """
        self.colony = colony
        self.current_position = colony.start
        self.visited = []
        self.visited.append(self.current_position)
        self.travel_time = 0
        self.prev_position = -1

    def next_node(self):
        """
        Choose next node where ant is going, based on pheromones already on the map.
        """
        # create list of possible next nodes
        possible_nodes = []
        for i in range(len(self.colony.map)):
            if i not in self.visited:
                possible_nodes.append(i)

        # calculate denominator
        den = 0
        for i in possible_nodes:
            den += self.colony.map.pheromones[self.current_position][i] ** self.colony.alpha \
                   * self.colony.map.heuristic[self.current_position][i] ** self.colony.beta

        # calculate probabilities for each next node
        probabilities = []
        for i in range(len(self.colony.map)):
            if i in possible_nodes:
                probabilities.append(self.colony.map.pheromones[self.current_position][i] ** self.colony.alpha
                                     * self.colony.map.heuristic[self.current_position][i] ** self.colony.beta / den)
        probabilities = np.asarray(probabilities)
        possible_nodes = np.asarray(possible_nodes)

        # select next node
        my_next_node = np.random.choice(a=possible_nodes, p=probabilities)
        self.prev_position = self.current_position
        self.visited.append(my_next_node)
        self.travel_time += self.colony.map.matrix[self.current_position][my_next_node]
        self.current_position = my_next_node

