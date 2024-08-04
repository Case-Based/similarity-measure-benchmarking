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
from src.utils.k_nearest_neighbour import get_k_nearest_neighbours


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


def get_5_nearest_neighbours_euclidian():
    get_k_nearest_neighbours(
        target_entry=target_benchmark_entry,
        data=benchmark_data,
        distance_fn=euc_calculate_distance,
        k=5,
    )


def get_5_nearest_neighbours_squared_euclidian():
    get_k_nearest_neighbours(
        target_entry=target_benchmark_entry,
        data=benchmark_data,
        distance_fn=sq_euc_calculate_distance,
        k=5,
    )


def get_5_nearest_neighbours_manhatten():
    get_k_nearest_neighbours(
        target_entry=target_benchmark_entry,
        data=benchmark_data,
        distance_fn=man_calculate_distance,
        k=5,
    )


def get_5_nearest_neighbours_canberra():
    get_k_nearest_neighbours(
        target_entry=target_benchmark_entry,
        data=benchmark_data,
        distance_fn=can_calculate_distance,
        k=5,
    )


def get_5_nearest_neighbours_chebychev():
    get_k_nearest_neighbours(
        target_entry=target_benchmark_entry,
        data=benchmark_data,
        distance_fn=che_calculate_distance,
        k=5,
    )


def get_5_nearest_neighbours_cosine():
    get_k_nearest_neighbours(
        target_entry=target_benchmark_entry,
        data=benchmark_data,
        distance_fn=cos_calculate_distance,
        k=5,
    )


def get_5_nearest_neighbours_pearson():
    get_k_nearest_neighbours(
        target_entry=target_benchmark_entry,
        data=benchmark_data,
        distance_fn=pea_calculate_distance,
        k=5,
    )


def get_10_nearest_neighbours_squared_euclidian():
    get_k_nearest_neighbours(
        target_entry=target_benchmark_entry,
        data=benchmark_data,
        distance_fn=sq_euc_calculate_distance,
        k=10,
    )


def get_10_nearest_neighbours_euclidian():
    get_k_nearest_neighbours(
        target_entry=target_benchmark_entry,
        data=benchmark_data,
        distance_fn=euc_calculate_distance,
        k=10,
    )


def get_10_nearest_neighbours_manhatten():
    get_k_nearest_neighbours(
        target_entry=target_benchmark_entry,
        data=benchmark_data,
        distance_fn=man_calculate_distance,
        k=10,
    )


def get_10_nearest_neighbours_canberra():
    get_k_nearest_neighbours(
        target_entry=target_benchmark_entry,
        data=benchmark_data,
        distance_fn=can_calculate_distance,
        k=10,
    )


def get_10_nearest_neighbours_chebychev():
    get_k_nearest_neighbours(
        target_entry=target_benchmark_entry,
        data=benchmark_data,
        distance_fn=che_calculate_distance,
        k=10,
    )


def get_10_nearest_neighbours_cosine():
    get_k_nearest_neighbours(
        target_entry=target_benchmark_entry,
        data=benchmark_data,
        distance_fn=cos_calculate_distance,
        k=10,
    )


def get_10_nearest_neighbours_pearson():
    get_k_nearest_neighbours(
        target_entry=target_benchmark_entry,
        data=benchmark_data,
        distance_fn=pea_calculate_distance,
        k=10,
    )


__benchmarks__ = [
    (
        get_5_nearest_neighbours_euclidian,
        get_5_nearest_neighbours_squared_euclidian,
        "5 nearest neighbours euclidian distance vs. squared euclidian distance",
    ),
    (
        get_5_nearest_neighbours_euclidian,
        get_5_nearest_neighbours_manhatten,
        "5 nearest neighbours euclidian distance vs. manhatten distance",
    ),
    (
        get_5_nearest_neighbours_euclidian,
        get_5_nearest_neighbours_canberra,
        "5 nearest neighbours euclidian distance vs. canberra distance",
    ),
    (
        get_5_nearest_neighbours_euclidian,
        get_5_nearest_neighbours_chebychev,
        "5 nearest neighbours euclidian distance vs. chebychev distance",
    ),
    (
        get_5_nearest_neighbours_euclidian,
        get_5_nearest_neighbours_cosine,
        "5 nearest neighbours euclidian distance vs. cosine distance",
    ),
    (
        get_5_nearest_neighbours_euclidian,
        get_5_nearest_neighbours_pearson,
        "5 nearest neighbours euclidian distance vs. pearson distance",
    ),
    (
        get_5_nearest_neighbours_squared_euclidian,
        get_5_nearest_neighbours_manhatten,
        "5 nearest neighbours squared euclidian distance vs. manhatten distance",
    ),
    (
        get_5_nearest_neighbours_squared_euclidian,
        get_5_nearest_neighbours_canberra,
        "5 nearest neighbours squared euclidian distance vs. canberra distance",
    ),
    (
        get_5_nearest_neighbours_squared_euclidian,
        get_5_nearest_neighbours_chebychev,
        "5 nearest neighbours squared euclidian distance vs. chebychev distance",
    ),
    (
        get_5_nearest_neighbours_squared_euclidian,
        get_5_nearest_neighbours_cosine,
        "5 nearest neighbours squared euclidian distance vs. cosine distance",
    ),
    (
        get_5_nearest_neighbours_squared_euclidian,
        get_5_nearest_neighbours_pearson,
        "5 nearest neighbours squared euclidian distance vs. pearson distance",
    ),
    (
        get_5_nearest_neighbours_manhatten,
        get_5_nearest_neighbours_canberra,
        "5 nearest neighbours manhatten distance vs. canberra distance",
    ),
    (
        get_5_nearest_neighbours_manhatten,
        get_5_nearest_neighbours_chebychev,
        "5 nearest neighbours manhatten distance vs. chebychev distance",
    ),
    (
        get_5_nearest_neighbours_manhatten,
        get_5_nearest_neighbours_cosine,
        "5 nearest neighbours manhatten distance vs. cosine distance",
    ),
    (
        get_5_nearest_neighbours_manhatten,
        get_5_nearest_neighbours_pearson,
        "5 nearest neighbours manhatten distance vs. pearson distance",
    ),
    (
        get_5_nearest_neighbours_canberra,
        get_5_nearest_neighbours_chebychev,
        "5 nearest neighbours canberra distance vs. chebychev distance",
    ),
    (
        get_5_nearest_neighbours_canberra,
        get_5_nearest_neighbours_cosine,
        "5 nearest neighbours canberra distance vs. cosine distance",
    ),
    (
        get_5_nearest_neighbours_canberra,
        get_5_nearest_neighbours_pearson,
        "5 nearest neighbours canberra distance vs. pearson distance",
    ),
    (
        get_5_nearest_neighbours_chebychev,
        get_5_nearest_neighbours_cosine,
        "5 nearest neighbours chebychev distance vs. cosine distance",
    ),
    (
        get_5_nearest_neighbours_chebychev,
        get_5_nearest_neighbours_pearson,
        "5 nearest neighbours chebychev distance vs. pearson distance",
    ),
    (
        get_5_nearest_neighbours_cosine,
        get_5_nearest_neighbours_pearson,
        "5 nearest neighbours cosine distance vs. pearson distance",
    ),
    (
        get_10_nearest_neighbours_euclidian,
        get_10_nearest_neighbours_squared_euclidian,
        "10 nearest neighbours euclidian distance vs. squared euclidian distance",
    ),
    (
        get_10_nearest_neighbours_euclidian,
        get_10_nearest_neighbours_manhatten,
        "10 nearest neighbours euclidian distance vs. manhatten distance",
    ),
    (
        get_10_nearest_neighbours_euclidian,
        get_10_nearest_neighbours_canberra,
        "10 nearest neighbours euclidian distance vs. canberra distance",
    ),
    (
        get_10_nearest_neighbours_euclidian,
        get_10_nearest_neighbours_chebychev,
        "10 nearest neighbours euclidian distance vs. chebychev distance",
    ),
    (
        get_10_nearest_neighbours_euclidian,
        get_10_nearest_neighbours_cosine,
        "10 nearest neighbours euclidian distance vs. cosine distance",
    ),
    (
        get_10_nearest_neighbours_euclidian,
        get_10_nearest_neighbours_pearson,
        "10 nearest neighbours euclidian distance vs. pearson distance",
    ),
    (
        get_10_nearest_neighbours_squared_euclidian,
        get_10_nearest_neighbours_manhatten,
        "10 nearest neighbours squared euclidian distance vs. manhatten distance",
    ),
    (
        get_10_nearest_neighbours_squared_euclidian,
        get_10_nearest_neighbours_canberra,
        "10 nearest neighbours squared euclidian distance vs. canberra distance",
    ),
    (
        get_10_nearest_neighbours_squared_euclidian,
        get_10_nearest_neighbours_chebychev,
        "10 nearest neighbours squared euclidian distance vs. chebychev distance",
    ),
    (
        get_10_nearest_neighbours_squared_euclidian,
        get_10_nearest_neighbours_cosine,
        "10 nearest neighbours squared euclidian distance vs. cosine distance",
    ),
    (
        get_10_nearest_neighbours_squared_euclidian,
        get_10_nearest_neighbours_pearson,
        "10 nearest neighbours squared euclidian distance vs. pearson distance",
    ),
    (
        get_10_nearest_neighbours_manhatten,
        get_10_nearest_neighbours_canberra,
        "10 nearest neighbours manhatten distance vs. canberra distance",
    ),
    (
        get_10_nearest_neighbours_manhatten,
        get_10_nearest_neighbours_chebychev,
        "10 nearest neighbours manhatten distance vs. chebychev distance",
    ),
    (
        get_10_nearest_neighbours_manhatten,
        get_10_nearest_neighbours_cosine,
        "10 nearest neighbours manhatten distance vs. cosine distance",
    ),
    (
        get_10_nearest_neighbours_manhatten,
        get_10_nearest_neighbours_pearson,
        "10 nearest neighbours manhatten distance vs. pearson distance",
    ),
    (
        get_10_nearest_neighbours_canberra,
        get_10_nearest_neighbours_chebychev,
        "10 nearest neighbours canberra distance vs. chebychev distance",
    ),
    (
        get_10_nearest_neighbours_canberra,
        get_10_nearest_neighbours_cosine,
        "10 nearest neighbours canberra distance vs. cosine distance",
    ),
    (
        get_10_nearest_neighbours_canberra,
        get_10_nearest_neighbours_pearson,
        "10 nearest neighbours canberra distance vs. pearson distance",
    ),
    (
        get_10_nearest_neighbours_chebychev,
        get_10_nearest_neighbours_cosine,
        "10 nearest neighbours chebychev distance vs. cosine distance",
    ),
    (
        get_10_nearest_neighbours_chebychev,
        get_10_nearest_neighbours_pearson,
        "10 nearest neighbours chebychev distance vs. pearson distance",
    ),
    (
        get_10_nearest_neighbours_cosine,
        get_10_nearest_neighbours_pearson,
        "10 nearest neighbours cosine distance vs. pearson distance",
    ),
]
