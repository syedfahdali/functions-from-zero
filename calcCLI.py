import click
from mylib import calc


@click.group()
def calcCLI():
    pass


@calcCLI.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def add(a, b):
    click.echo(calc.add(a, b))


@calcCLI.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def subtract(a, b):
    click.echo(calc.subtract(a, b))


@calcCLI.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def multiply(a, b):
    click.echo(calc.multiply(a, b))


@calcCLI.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def divide(a, b):
    click.echo(calc.divide(a, b))


@calcCLI.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def power(a, b):
    click.echo(calc.power(a, b))
