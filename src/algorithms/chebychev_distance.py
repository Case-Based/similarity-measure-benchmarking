from typing import Union


def calculate_distance(
    first_entry: list[Union[int, float]], second_entry: list[Union[int, float]]
) -> float:
    """
    Calculate the distance between two data entries by using the chebychev distance.
    :param first_entry: list
    :param second_entry: list
    :return: float
    """
    highest_value = 0
    for index in range(min(len(first_entry), len(second_entry))):
        distance = abs(first_entry[index] - second_entry[index])
        if distance > highest_value:
            highest_value = distance
    return highest_value
