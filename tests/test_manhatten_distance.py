from algorithms.manhatten_distance import calculate_distance


TEST_TARGET_ENTRY = [1, 4, 9]
TEST_DATA = [[1, 2, 3], [10, 40, 90], [2, 6, 10], [12.4, 23.4, 1.3], [0.5, 1.2, 3.4]]
EXPECTED_DISTANCES = [
    8,
    126,
    4,
    38.5,
    8.9,
]
EXPECTED_NEIGHBOURS = [[1, 2, 3], [2, 6, 10], [0.5, 1.2, 3.4]]


def test_manhatten_distance():
    for index, entry in enumerate(TEST_DATA):
        distance = calculate_distance(TEST_TARGET_ENTRY, entry)
        assert round(distance, 2) == EXPECTED_DISTANCES[index]
