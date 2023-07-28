# import math


def value_in_percentage(
        percentage: float | int | str,
        total: float | int | str,
) -> float:
    try:
        return float(percentage) * float(total) / 100
    except ZeroDivisionError:
        return 0


def percentage_hits(
        total: int | float | str,
        hits: int | float | str
) -> float:
    try:
        return float(hits) / float(total) * 100
    except ZeroDivisionError:
        return 0


if __name__ == "__main__":

    print(percentage_hits(100, 50))
    print(value_in_percentage(9, 5))
