def calculate_distance(first_entry: list, second_entry: list) -> float:
    """
    Calculate the distance between two data entries by using the squared euclidian distance.
    The squared euclidian distance is calculated as follows:
    d(P, Q) = (p1 - q1)^2 + (p2 - q2)^2 + ... + (pn - qn)^2
    :param first_entry: list
    :param second_entry: list
    :return: float
    """
    summary = 0.0
    for i in range(min(len(first_entry), len(second_entry))):
        summary += (first_entry[i] - second_entry[i]) ** 2
    return summary
