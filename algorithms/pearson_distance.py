from typing import Union
from utils.operators import safe_division
from math import sqrt


def calculate_distance(
    first_entry: list[Union[int, float]], second_entry: list[Union[int, float]]
) -> float:
    data_length = min(len(first_entry), len(second_entry))
    p_mean = 0.0
    q_mean = 0.0
    for index in range(data_length):
        p_mean += first_entry[index]
        q_mean += second_entry[index]
    p_mean = safe_division(p_mean, data_length)
    q_mean = safe_division(q_mean, data_length)
    p_variance = 0.0
    q_variance = 0.0
    covariance = 0.0
    for index in range(data_length):
        p_variance += (first_entry[index] - p_mean) ** 2
        q_variance += (second_entry[index] - q_mean) ** 2
        covariance += (first_entry[index] - p_mean) * (second_entry[index] - q_mean)
    p_variance = sqrt(safe_division(p_variance, data_length))
    q_variance = sqrt(safe_division(q_variance, data_length))
    covariance = safe_division(covariance, data_length)
    return 1 - safe_division(covariance, p_variance * q_variance)
