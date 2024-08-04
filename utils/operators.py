from typing import Union


def safe_division(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a / b if 0 not in (a, b) else 0
