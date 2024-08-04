from typing import Union


def safe_division(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a / b if 0 not in (a, b) else 0


def calculate_mean(data: list[Union[int, float]]) -> float:
    mean = 0.0
    for entry in data:
        mean += entry
    return safe_division(mean, len(data))


def calculate_variance(data: list[Union[int, float]], mean: Union[int, float]) -> float:
    variance = 0.0
    for entry in data:
        variance += (entry - mean) ** 2
    return safe_division(variance, len(data))


def calculate_covariance(
    data_1: list[Union[int, float]],
    data_2: list[Union[int, float]],
    mean_1: Union[int, float],
    mean_2: Union[int, float],
) -> float:
    data_length = min(len(data_1), len(data_2))
    covariance = 0.0
    for index in range(data_length):
        covariance += (data_1[index] - mean_1) * (data_2[index] - mean_2)
    return safe_division(covariance, data_length)


def traverse_matrx(matrix: list[list]):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
