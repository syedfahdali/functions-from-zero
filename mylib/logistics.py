"""
This module deals with logistics and calculates distances between two points and 
the time it takes to travel between two points and other logistics-related functions 
for a given speed.
"""

from geopy.distance import geodesic

# A list of 10 cities in the US with their latitude and longitude
CITY_DATA = [
    ("New York", (40.7128, -74.0060)),
    ("Los Angeles", (34.0522, -118.2437)),
    ("Chicago", (41.8781, -87.6298)),
    ("Houston", (29.7604, -95.3698)),
    ("Phoenix", (33.4484, -112.0740)),
    ("Philadelphia", (39.9526, -75.1652)),
    ("San Antonio", (29.4241, -98.4936)),
    ("San Diego", (32.7157, -117.1611)),
    ("Dallas", (32.7767, -96.7970)),
    ("San Jose", (37.3382, -121.8863)),
]


def distance_between_points(point1, point2):
    """
    Calculate the distance between two points using geopy.
    """
    return geodesic(point1, point2).kilometers


def find_coordinates(city):
    """
    Extract the coordinates from a city tuple.
    """
    return city[1]


def total_distance(city_list):
    """
    Calculate the total distance between all cities in the list.
    """
    total = 0
    for i in range(len(city_list) - 1):
        total += distance_between_points(city_list[i][1], city_list[i + 1][1])
    return total


def print_cities():
    """Prints the names of all cities in the list."""
    for city in CITY_DATA:
        print(city[0])


if __name__ == "__main__":
    print("Total distance between all cities: ", total_distance(CITY_DATA), "km")
    print_cities()
