""" Tests for the compute module
"""
from nose.tools import assert_equal

from sprint_tutorial.compute import my_sum


def test_my_sum1():
    assert_equal(my_sum(0, 0), 0)


def test_my_sum2():
    assert_equal(my_sum(1, -1), 0)


def nonint_my_sum_test_1():
    """A test of my sum for non-integers."""
    assert_equal(my_sum(float(1), float(1)), float(2))


def nonint_my_sum_test_2():
    """Another test for nonints."""
    assert_equal(my_sum(0.5, 0.5), float(1))
