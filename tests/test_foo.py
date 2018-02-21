import pytest
from src.foo import *

def test_add():
    assert add(1,2) == 3
    assert add(0,0) == 0
    assert add(3,-1) == 2
    assert add(-1,3) == 2

def test_sub():
    assert sub(1,2) == 0
    assert sub(0,0) == 0
    assert sub(3,-1) == 4
    assert sub(-1,3) == -4
