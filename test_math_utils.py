import pytest
from MathUtils import MathUtils  

@pytest.fixture
def setup_resources():
    yield

def test_add():
    assert MathUtils.add(2, 3) == 5
    assert MathUtils.add(-5, 7) == 2
    assert MathUtils.add(0, 0) == 0

def test_subtract():
    assert MathUtils.subtract(10, 5) == 5
    assert MathUtils.subtract(3, 8) == -5
    assert MathUtils.subtract(0, 0) == 0

def test_multiply():
    assert MathUtils
