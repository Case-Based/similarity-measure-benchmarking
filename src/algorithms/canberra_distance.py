from typing import Union
from src.utils.operators import safe_division


def calculate_distance(
    first_entry: list[Union[int, float]], second_entry: list[Union[int, float]]
) -> float:
    """
    Calculate the distance between two data entries by using the canberra distance.
    :param first_entry: list
    :param second_entry: list
    :return: float
    """
    distance = 0.0
    for index in range(min(len(first_entry), len(second_entry))):
        distance += safe_division(
            abs(first_entry[index] - second_entry[index]),
            abs(first_entry[index] + second_entry[index]),
        )
    return distance
