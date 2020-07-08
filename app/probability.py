# -*- coding: utf-8 -*-
"""Probability birthday in days range

Example:
    $ python probability.py --ydays 365 --pcnt 8 --drange 7

Variables has default values.

"""

import math
import sys
from argparse import ArgumentParser


def probability(ydays: int, pcnt: int, drange: int) -> int:
    """
    Calculate probability
    :param ydays: int
    :param pcnt: int
    :param drange: int
    :return: int
    """
    return math.ceil(
        (
            1
            - math.factorial(ydays - pcnt * drange - 1)
            / (
                ydays ** (pcnt - 1)
                * math.factorial(ydays - pcnt * (drange + 1))
            )
        )
        * 100
    )


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-y", "--ydays", type=int, default=365, help="days count"
    )
    parser.add_argument(
        "-p", "--pcnt", type=int, default=8, help="peoples count"
    )
    parser.add_argument(
        "-d", "--drange", type=int, default=7, help="days range"
    )
    args = parser.parse_args()

    result = probability(args.ydays, args.pcnt, args.drange)
    sys.stdout.write(f"Probability: {result}%")
