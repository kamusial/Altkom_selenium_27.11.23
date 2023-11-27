from pytest_kod import *
import pytest

def test_multiply():
    assert multiply(5, 6) == 30
    assert multiply(100, 1.1) == 110
    assert multiply(0.0001, 1) == 0.0001
    assert multiply(1, 'mama') == 1


