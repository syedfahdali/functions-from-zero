from mylib.logistics import (
    CITY_DATA,
    distance_between_points,
  
)

import click

@click.group()
def cli():
    """
    A simple CLI for logistics calculations.
    """
      # If you want to avoid W0107, remove this line


@click.command("distance")
@click.argument("city1")
@click.argument("city2")
def distance_between_cities(city1, city2):
    """
    Calculate the distance between two cities by their names.
    """
    # Find the coordinates from CITY_DATA based on city names
    city_lookup = {name: coords for name, coords in CITY_DATA}
    if city1 not in city_lookup or city2 not in city_lookup:
        click.echo("One or both city names are invalid.")
        return

    point1 = city_lookup[city1]
    point2 = city_lookup[city2]
    distance = distance_between_points(point1, point2)
    click.echo(f"The distance between {city1} and {city2} is {distance:.2f} km.")


@click.command("total-distance")
def total_distance_cli():
    """
    Calculate the total distance between all cities in the CITY_DATA list.
    """
    from mylib.logistics import total_distance
    total = total_distance(CITY_DATA)
    click.echo(f"The total distance between all cities is {total:.2f} km.")


# Register commands
cli.add_command(distance_between_cities)
cli.add_command(total_distance_cli)

if __name__ == "__main__":
    cli()
