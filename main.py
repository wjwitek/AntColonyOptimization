from src.colony import Colony
import numpy as np

TEST_MAP_1 = np.array([(1,1), (1,2), (2,1), (3,6), (3,-1), (5,1)])
TEST_MAP_2 = 0  # TODO

ALPHA = 0.2
ITERATIONS = 100
INTENSITY = 5
ANTS_NO = 100
EVAPORATION = 0.5
BETA = 0.05

colony = Colony(TEST_MAP_1, ALPHA, ITERATIONS, INTENSITY, ANTS_NO, EVAPORATION, BETA)
