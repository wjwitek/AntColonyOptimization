import time

from src.colony import Colony
from src.visualization import browse_images
import numpy as np
import os

TEST_MAP_1 = np.array([(1,1), (1,2), (2,1), (3,6), (3,-1), (5,1)])
TEST_MAP_2 = np.array([(np.cos(i), np.sin(i)) for i in range(0, 360, 30)])
TEST_MAP_3 = np.array([(np.random.random(), np.random.random()) for i in range(20)])
TEST_MAP_4 = np.array([(3*(-1)**j*k+i*(1-k), 3*(-1)**j*(1-k)+i*k) for k in range(0, 2) for j in range(0, 2) for i in range(-2, 3)])
# TEST_MAP_4 = np.array([(-2, -2), (-2, 0), (-2, 2), (2, -2), (2, 0), (2, 2), (), (), (), (), (), (), ])
print(TEST_MAP_3)
print(TEST_MAP_4)

# ALPHA = 0.2
# ITERATIONS = 10
# INTENSITY = 5
# ANTS_NO = 100
# EVAPORATION = 0.5
# BETA = 0.05

ALPHA = 0.4
ITERATIONS = 150
INTENSITY = 30
ANTS_NO = 3000
EVAPORATION = 0.5
BETA = 0.05

start = time.time()
colony = Colony(TEST_MAP_4, ALPHA, ITERATIONS, INTENSITY, ANTS_NO, EVAPORATION, BETA)

results = colony.solve_route()
print((time.time()-start)/60)

browse_images(results[0])

i = 0
while True:
    try:
        os.remove(f"img_{i}.jpg")
        i += 1
    except FileNotFoundError:
        break
