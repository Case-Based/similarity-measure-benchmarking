from typing import Union


def calculate_distance(
    first_entry: list[Union[int, float]], second_entry: list[Union[int, float]]
) -> float:
    """
    Calculate the distance between two data entries by using the manhatten distance.
    The manhatten distance is calculated as follows:
    d(P, Q) = |p1 - q1| + |p2 - q2| + ... |pn - qn|
    :param first_entry: list
    :param second_entry: list
    :return: float
    """
    summary = 0.0
    for i in range(min(len(first_entry), len(second_entry))):
        summary += abs(first_entry[i] - second_entry[i])
    return summary
