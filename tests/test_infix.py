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

def test_apply_operation_no_parentheses():
    # Setup
    desired = ['+ 1 2']

    # Exercise
    CalcInfix = CalculatorInfix()
    CalcInfix._stack = ["1", "2"]
    CalcInfix._operator_stack = ["+"]
    CalcInfix._apply_operation_no_parentheses()
    actual = CalcInfix._stack

    # Verify
    assert actual == desired
    # Cleanup - none necessary
