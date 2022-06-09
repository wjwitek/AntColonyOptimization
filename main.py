from src.colony import Colony
from src.visualization import browse_images
import numpy as np
import os

# TEST_MAP_1 = np.array([(1,1), (1,2), (2,1), (3,6), (3,-1), (5,1)])
TEST_MAP_1 = np.array([(np.cos(i), np.sin(i)) for i in range(0, 360, 30)])
# TEST_MAP_1 = np.array([(np.random.random(), np.random.random()) for i in range(15)])
# print(TEST_MAP_1)
TEST_MAP_2 = 0  # TODO

# ALPHA = 0.2
# ITERATIONS = 10
# INTENSITY = 5
# ANTS_NO = 100
# EVAPORATION = 0.5
# BETA = 0.05

ALPHA = 0.3
ITERATIONS = 40
INTENSITY = 25
ANTS_NO = 1000
EVAPORATION = 0.8
BETA = 0.05

colony = Colony(TEST_MAP_1, ALPHA, ITERATIONS, INTENSITY, ANTS_NO, EVAPORATION, BETA)

results = colony.solve_route()

browse_images(results[0])

i = 0
while True:
    try:
        os.remove(f"img_{i}.jpg")
        i += 1
    except FileNotFoundError:
        break
