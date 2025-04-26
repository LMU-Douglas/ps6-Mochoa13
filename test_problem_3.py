import pytest
from xylophone import *
# -------------------------------
# Tests for Problem 3: Xylophone
# -------------------------------

def test_cost_no_purchase_needed():
    assert cost_of_bars("7 6 5") == 0

def test_cost_basic_gap():
    assert cost_of_bars("1 4 2") == 3

def test_cost_reverse_order():
    assert cost_of_bars("6 3 8") == 16

def test_cost_with_larger_gap():
    assert cost_of_bars("1 4 6") == 10
    
def test_major_gap():
    assert cost_of_bars("1 10 5") == 39

