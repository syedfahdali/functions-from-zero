# test_calc.py

import pytest
from mylib import calc
from calcCLI import calcCLI
from click.testing import CliRunner

# ------------------------------
# Function tests using pytest
# ------------------------------


def test_add():
    assert calc.add(2, 3) == 5


def test_subtract():
    assert calc.subtract(10, 4) == 6


def test_multiply():
    assert calc.multiply(3, 7) == 21


def test_divide():
    assert calc.divide(8, 2) == 4
    assert calc.divide(5, 0) == "Error: Division by zero"


def test_power():
    assert calc.power(2, 3) == 8


# ------------------------------
# CLI tests using click.testing
# ------------------------------


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_add(runner):
    result = runner.invoke(calcCLI, ["add", "2", "3"])
    assert result.exit_code == 0
    assert "5" in result.output


def test_cli_divide_by_zero(runner):
    result = runner.invoke(calcCLI, ["divide", "5", "0"])
    assert result.exit_code == 0
    assert "Error" in result.output
