from src.algorithms.euclidian_distance import calculate_distance
from src.utils.k_nearest_neighbour import get_k_nearest_neighbours


TEST_TARGET_ENTRY = [1, 4, 9]
TEST_DATA = [[1, 2, 3], [10, 40, 90], [2, 6, 10], [12.4, 23.4, 1.3], [0.5, 1.2, 3.4]]
EXPECTED_DISTANCES = [
    6.32,
    89.10,
    2.45,
    23.78,
    6.28,
]
EXPECTED_NEIGHBOURS = [[1, 2, 3], [2, 6, 10], [0.5, 1.2, 3.4]]


def test_euclidian_distance():
    for index, entry in enumerate(TEST_DATA):
        distance = calculate_distance(TEST_TARGET_ENTRY, entry)
        assert round(distance, 2) == EXPECTED_DISTANCES[index]


def test_euclidian_distance_3_neighbours():
    neighbours = get_k_nearest_neighbours(
        target_entry=TEST_TARGET_ENTRY,
        data=TEST_DATA,
        distance_fn=calculate_distance,
        k=3,
    )
    for neighbour in neighbours:
        assert neighbour.entry in EXPECTED_NEIGHBOURS
