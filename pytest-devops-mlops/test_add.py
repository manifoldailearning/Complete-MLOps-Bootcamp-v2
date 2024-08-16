import pytest 
from main import add

def test_addition():
    assert add(3,4) == 7
    assert add(1,1) == 2
    assert add(-1,-2) == -4