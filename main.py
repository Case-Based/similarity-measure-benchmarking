from utils.k_nearest_neighbour import get_k_nearest_neighbours
from algorithms.squared_euclidian_distance import calculate_distance

data = [[1, 2, 4], [4, 9, 1], [12.4, 99.6, 19.2], [0.45, 12.2, 45.5], [1, 4.5, 2.3]]

print(get_k_nearest_neighbours([1, 2, 3], data, calculate_distance))
