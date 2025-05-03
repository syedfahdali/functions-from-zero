"""
This module deals with logistics and calculates distances between two points and the time it takes to travel between two points and other logistics-related functions for a given speed.
"""
# build a list of 10 cities in the US with their latitude and longitude

cities = [
    ("New York", (40.7128, -74.0060)),
    ("Los Angeles", (34.0522, -118.2437)),
    ("Chicago", (41.8781, -87.6298)),
    ("Houston", (29.7604, -95.3698)),
    ("Phoenix", (33.4484, -112.0740)),
    ("Philadelphia", (39.9526, -75.1652)),
    ("San Antonio", (29.4241, -98.4936)),
    ("San Diego", (32.7157, -117.1611)),
    ("Dallas", (32.7767, -96.7970)),
    ("San Jose", (37.3382, -121.8863))
]

import geopy
from geopy.distance import geodesic
def distance_between_points(point1, point2):
    """
    Calculate the distance between two points using geopy.
    
    Args:
        point1 (tuple): A tuple containing the latitude and longitude of the first point.
        point2 (tuple): A tuple containing the latitude and longitude of the second point.
    
    Returns:
        float: The distance between the two points in kilometers.
    """
    
    return geodesic(point1, point2).kilometers 

def find_coordinates(city):
    """
    Find the coordinates of a city using geopy.
    
    Args:
        city (str): The name of the city.
    
    Returns:
        tuple: A tuple containing the latitude and longitude of the city.
    """
    return city.latitude, city.longitude


def total_distance(cities):
    """
    Calculate the total distance between all cities in the list.
    
    Args:
        cities (list): A list of tuples containing the name and coordinates of the cities.
    
    Returns:
        float: The total distance between all cities in kilometers.
    """
    
    total_distance = 0
    for i in range(len(cities) - 1):
        total_distance += distance_between_points(cities[i][1], cities[i + 1][1])
    return total_distance

print("Total distance between all cities: ", total_distance(cities), "km")

def print_cities():
    for city in cities:
        print(city[0])

print_cities()