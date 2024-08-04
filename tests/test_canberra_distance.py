from algorithms.canberra_distance import calculate_distance


TEST_TARGET_ENTRY = [1, 4, 9]
TEST_DATA = [[1, 2, 3], [10, 40, 90], [2, 6, 10], [12.4, 23.4, 1.3], [0.5, 1.2, 3.4]]
EXPECTED_DISTANCES = [
    0.83,
    2.45,
    0.59,
    2.31,
    1.32,
]
EXPECTED_NEIGHBOURS = [[1, 2, 3], [2, 6, 10], [0.5, 1.2, 3.4]]


def test_canberra_distance():
    for index, entry in enumerate(TEST_DATA):
        assert (
            round(calculate_distance(TEST_TARGET_ENTRY, entry), 2)
            == EXPECTED_DISTANCES[index]
        )
