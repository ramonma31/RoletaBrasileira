# import math


def value_in_percentage(
        percentage: float | int | str,
        total: float | int | str,
) -> float:

    if type(percentage) == str or type(total) == str:
        return float(percentage) * float(total) / 100

    return percentage * total / 100


def percentage_hits(
        total: int | float | str,
        hits: int | float | str
) -> float:

    if type(total) == str or type(hits):
        return float(total) * 100 / float(hits)

    return float(total) * 100 / float(hits)
