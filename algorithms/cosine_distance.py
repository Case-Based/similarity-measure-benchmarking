from typing import Union
from utils.operators import safe_division
from math import sqrt


def calculate_distance(
    first_entry: list[Union[int, float]], second_entry: list[Union[int, float]]
) -> float:
    """
    Calculate the distance between two data entries by using the cosine distance.
    :param first_entry: list
    :param second_entry: list
    :return: float
    """
    data_length = min(len(first_entry), len(second_entry))
    p_sum = 0.0
    q_sum = 0.0
    pq_sum = 0.0
    for index in range(data_length):
        pq_sum += first_entry[index] * second_entry[index]
        p_sum += first_entry[index] ** 2
        q_sum += second_entry[index] ** 2
    return 1 - safe_division(pq_sum, sqrt(p_sum) * sqrt(q_sum))
