from dataclasses import dataclass
from typing import Union


@dataclass
class SimilarityEntry:
    distance: float
    entry: list[Union[int, float]]
