import pytest 
# write tests for logisticsCLI
from mylib.logistics import cities, distance_between_points, total_distance

def distance_between_two_points():
    assert distance_between_points(cities[0][1],cities[1][1]) == 2449.349999999995

