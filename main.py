from utils.k_nearest_neighbour import get_k_nearest_neighbours
from algorithms.euclidian_distance import calculate_distance

data = [[1, 2, 3], [10, 40, 90], [2, 6, 10], [12.4, 23.4, 1.3], [0.5, 1.2, 3.4]]

print(get_k_nearest_neighbours([1, 4, 9], data, calculate_distance, 5))
