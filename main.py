from src.colony import Colony
import numpy as np

test_matrix = np.asarray([[float('inf'), 1, 2], [3, float('inf'), 1], [1, 3, float('inf')]])
colony = Colony(test_matrix, 0.2, 10, 5, 10, 0.4)
print(colony.solve_route())
