#!/usr/bin/env python3
# -*- coding: latin-1 -*-

from kmt_calculator import CalculatorInfix

""" Unit tests for CalculatorInfix class
"""


def test_inheritance():
    # Setup
    desired = ["2", "1", "*", "1", "1", "+", "10", "/", "-"]

    # Exercise
    actual = CalculatorInfix._split_and_reverse_expression("- / 10 + 1 1 * 1 2")

    # Verify
    assert all([a == b for a, b in zip(actual, desired)])
    # Cleanup - none necessary