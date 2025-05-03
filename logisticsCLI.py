from mylib.logistics import cities, distance_between_points, find_coordinates, total_distance
import click

#build a click group 
@click.group() 
def cli():
    """"
    A simple CLI for logistics calculations.
    """

@click.command("distance")
@click.command("city1")
@click.command("city2")

def distance_between_cities(city1, city2):
    """
    Calculate the distance between two cities.
    
    Args:
        city1 (str): The name of the first city.
        city2 (str): The name of the second city.
    
    Returns:
        float: The distance between the two cities in kilometers.
    """
    point1 = find_coordinates(city1)
    point2 = find_coordinates(city2)
    distance = distance_between_points(point1, point2)
    click.echo(f"The distance between {city1} and {city2} is {distance:.2f} km.")
def total_distance_cli():
    """
    Calculate the total distance between all cities in the list.
    
    Args:
        cities (list): A list of tuples containing the name and coordinates of the cities.
    
    Returns:
        float: The total distance between all cities in kilometers.
    """
    total_distance = total_distance(cities)
    click.echo(f"The total distance between all cities is {total_distance:.2f} km.")
    