import pytest

# write tests for logisticsCLI
from mylib.logistics import CITY_DATA, distance_between_points, total_distance


def distance_between_two_points():
    assert distance_between_points(CITY_DATA[0][1], CITY_DATA[1][1]) == 2449.349999999995
