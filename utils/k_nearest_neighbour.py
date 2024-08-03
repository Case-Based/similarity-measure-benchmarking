from typing import Callable, Union
from utils.types import SimilarityEntry


def get_k_nearest_neighbours(
    target_entry: list[Union[int, float]],
    data: list[list[Union[int, float]]],
    distance_fn: Callable[[list[Union[int, float]], list[Union[int, float]]], float],
    k: int = 3,
) -> list[SimilarityEntry]:
    """
    Get the k nearest neighbours of the target entry.
    The similarity measure algorithm can be configured providing a distance_fn function.
    After the similarity measure you will get a list with the k nearest neighbours.
    :param target_entry: list[Union[int, float]]
    :param data: list[list[Union[int, float]]]
    :param distance_fn: Callable[[list[Union[int, float]], list[Union[int, float]]], float]
    :param k: int (default 3)
    :return: list[SimilarityEntry]
    """
    nearest_neighbours: list[SimilarityEntry] = list()
    for entry in data:
        similarity = distance_fn(target_entry, entry)
        if len(nearest_neighbours) < k:
            nearest_neighbours.append(
                SimilarityEntry(
                    distance=similarity,
                    entry=entry,
                )
            )
        else:
            highest_distance = 0.0
            highest_distance_id = -1
            for index, value in enumerate(nearest_neighbours):
                if value.distance > similarity and value.distance > highest_distance:
                    highest_distance = similarity
                    highest_distance_id = index
            if highest_distance_id > -1:
                nearest_neighbours[highest_distance_id] = SimilarityEntry(
                    distance=similarity,
                    entry=entry,
                )
    return nearest_neighbours
