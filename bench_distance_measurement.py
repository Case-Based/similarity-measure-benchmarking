from csv import reader
from src.algorithms.euclidian_distance import (
    calculate_distance as euc_calculate_distance,
)
from src.algorithms.squared_euclidian_distance import (
    calculate_distance as sq_euc_calculate_distance,
)
from src.algorithms.manhatten_distance import (
    calculate_distance as man_calculate_distance,
)
from src.algorithms.chebychev_distance import (
    calculate_distance as che_calculate_distance,
)
from src.algorithms.cosine_distance import calculate_distance as cos_calculate_distance
from src.algorithms.pearson_distance import calculate_distance as pea_calculate_distance
from src.algorithms.canberra_distance import (
    calculate_distance as can_calculate_distance,
)


benchmark_data = list()

with open("dummy_data.csv", mode="r") as file:
    csv_reader = reader(file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        benchmark_data.append([float(val) for val in row])

target_benchmark_entry = [
    0.8399320421228295,
    0.8803089261228119,
    0.5465353529619043,
    0.9857457439505442,
    0.7170372083251881,
    0.21965358745932928,
    0.13686839330619405,
    0.3794558084825289,
    0.029704158132653924,
    0.7792274811566872,
]


def distance_calculation_euclidian():
    for entry in benchmark_data:
        euc_calculate_distance(target_benchmark_entry, entry)


def distance_calculation_squared_euclidian():
    for entry in benchmark_data:
        sq_euc_calculate_distance(target_benchmark_entry, entry)


def distance_manhatten():
    for entry in benchmark_data:
        man_calculate_distance(target_benchmark_entry, entry)


def distance_chebychev():
    for entry in benchmark_data:
        che_calculate_distance(target_benchmark_entry, entry)


def distance_cosine():
    for entry in benchmark_data:
        cos_calculate_distance(target_benchmark_entry, entry)


def distance_pearson():
    for entry in benchmark_data:
        pea_calculate_distance(target_benchmark_entry, entry)


def distance_canberra():
    for entry in benchmark_data:
        can_calculate_distance(target_benchmark_entry, entry)


__benchmarks__ = [
    (
        distance_calculation_euclidian,
        distance_calculation_squared_euclidian,
        "Euclidian distance vs. squared euclidian distance",
    ),
    (
        distance_calculation_euclidian,
        distance_manhatten,
        "Euclidian distance vs. manhatten distance",
    ),
    (
        distance_calculation_euclidian,
        distance_chebychev,
        "Euclidian distance vs. chebychev distance",
    ),
    (
        distance_calculation_euclidian,
        distance_cosine,
        "Euclidian distance vs. cosine distance",
    ),
    (
        distance_calculation_euclidian,
        distance_pearson,
        "Euclidian distance vs. pearson distance",
    ),
    (
        distance_calculation_euclidian,
        distance_canberra,
        "Euclidian distance vs. canberra distance",
    ),
    (
        distance_calculation_squared_euclidian,
        distance_manhatten,
        "Squared euclidian distance vs. manhatten distance",
    ),
    (
        distance_calculation_squared_euclidian,
        distance_chebychev,
        "Squared euclidian distance vs. chebychev distance",
    ),
    (
        distance_calculation_squared_euclidian,
        distance_cosine,
        "Squared euclidian distance vs. cosine distance",
    ),
    (
        distance_calculation_squared_euclidian,
        distance_pearson,
        "Squared euclidian distance vs. pearson distance",
    ),
    (
        distance_calculation_squared_euclidian,
        distance_canberra,
        "Squared euclidian distance vs. canberra distance",
    ),
    (
        distance_manhatten,
        distance_chebychev,
        "Manhatten distance vs. chebychev distance",
    ),
    (distance_manhatten, distance_cosine, "Manhatten distance vs. cosine distance"),
    (distance_manhatten, distance_pearson, "Manhatten distance vs. pearson distance"),
    (distance_manhatten, distance_canberra, "Manhatten distance vs. canberra distance"),
    (distance_chebychev, distance_cosine, "Chebychev distance vs. cosine distance"),
    (distance_chebychev, distance_pearson, "Chebychev distance vs. pearson distance"),
    (distance_chebychev, distance_canberra, "Chebychev distance vs. canberra distance"),
    (distance_cosine, distance_pearson, "Cosine distance vs. pearson distance"),
    (distance_cosine, distance_canberra, "Cosine distance vs. canberra distance"),
    (distance_pearson, distance_canberra, "Pearson distance vs. canberra distance"),
]
