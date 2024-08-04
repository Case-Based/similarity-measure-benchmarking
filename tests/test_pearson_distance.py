from algorithms.pearson_distance import calculate_distance


TEST_TARGET_ENTRY = [1, 4, 9]
TEST_DATA = [[1, 2, 3], [10, 40, 90], [2, 6, 10], [12.4, 23.4, 1.3], [0.5, 1.2, 3.4]]
EXPECTED_DISTANCES = [
    0.010256681389212985,
    -2.220446049250313e-16,
    0.010256681389212985,
    1.6206400913299066,
    0.010763298146088451,
]


def test_pearson_distance():
    for index, entry in enumerate(TEST_DATA):
        distance = calculate_distance(TEST_TARGET_ENTRY, entry)
        assert distance == EXPECTED_DISTANCES[index]
