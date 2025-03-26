import pytest
from simple_math import SimpleMath

@pytest.fixture
def simple_math():
    return SimpleMath()

@pytest.mark.parametrize("x, result", [
    (2, 4), (-3, 9), (0, 0) ])
def test_square(x, result, simple_math):
    assert simple_math.square(x) == result

@pytest.mark.parametrize("x, result", [
    (2, 8), (-3, -27), (0, 0) ])
def test_cube(x, result, simple_math):
    assert simple_math.cube(x) == result

