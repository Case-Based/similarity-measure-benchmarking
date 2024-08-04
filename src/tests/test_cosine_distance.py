from src.algorithms.cosine_distance import calculate_distance


TEST_TARGET_ENTRY = [1, 4, 9]
TEST_DATA = [[1, 2, 3], [10, 40, 90], [2, 6, 10], [12.4, 23.4, 1.3], [0.5, 1.2, 3.4]]
EXPECTED_DISTANCES = [
    0.02809,
    0.0,
    0.00967,
    0.55158,
    0.00374,
]
EXPECTED_NEIGHBOURS = [[1, 2, 3], [2, 6, 10], [0.5, 1.2, 3.4]]


def test_cosine_distance():
    for index, entry in enumerate(TEST_DATA):
        distance = calculate_distance(TEST_TARGET_ENTRY, entry)
        assert round(distance, 5) == EXPECTED_DISTANCES[index]
