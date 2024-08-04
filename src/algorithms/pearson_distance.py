from typing import Union
from src.utils.operators import (
    safe_division,
    calculate_mean,
    calculate_variance,
    calculate_covariance,
)
from math import sqrt


def calculate_distance(
    first_entry: list[Union[int, float]], second_entry: list[Union[int, float]]
) -> float:
    p_mean = calculate_mean(first_entry)
    q_mean = calculate_mean(second_entry)
    p_variance = sqrt(calculate_variance(first_entry, p_mean))
    q_variance = sqrt(calculate_variance(second_entry, q_mean))
    covariance = calculate_covariance(first_entry, second_entry, p_mean, q_mean)
    return 1 - safe_division(covariance, p_variance * q_variance)
