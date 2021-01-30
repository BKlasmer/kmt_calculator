#!/usr/bin/env python3
# -*- coding: latin-1 -*-

from kmt_calculator import CalculatorPrefix

""" Example boilerplate file
"""

def test_split_and_reverse_expression():
    # Setup
    desired = ['2', '1', '*', '1', '1', '+', '10', '/', '-']

    # Exercise
    actual = CalculatorPrefix._split_and_reverse_expression("- / 10 + 1 1 * 1 2")

    # Verify
    assert all([a == b for a, b in zip(actual, desired)])
    # Cleanup - none necessary

def test_perform_prefix_operation_add():
    # Setup
    desired = 9

    # Exercise
    CalcPrefix = CalculatorPrefix()
    CalcPrefix._stack = [3, 6]
    CalcPrefix._perform_prefix_operation("+")
    actual = CalcPrefix._stack[0]

    # Verify
    assert actual == desired
    # Cleanup - none necessary

def test_perform_prefix_operation_sub():
    # Setup
    desired = 3

    # Exercise
    CalcPrefix = CalculatorPrefix()
    CalcPrefix._stack = [3, 6]
    CalcPrefix._perform_prefix_operation("-")
    actual = CalcPrefix._stack[0]

    # Verify
    assert actual == desired
    # Cleanup - none necessary

def test_perform_prefix_operation_mult():
    # Setup
    desired = 18

    # Exercise
    CalcPrefix = CalculatorPrefix()
    CalcPrefix._stack = [3, 6]
    CalcPrefix._perform_prefix_operation("*")
    actual = CalcPrefix._stack[0]

    # Verify
    assert actual == desired
    # Cleanup - none necessary

def test_perform_prefix_operation_div():
    # Setup
    desired = 2

    # Exercise
    CalcPrefix = CalculatorPrefix()
    CalcPrefix._stack = [3, 6]
    CalcPrefix._perform_prefix_operation("/")
    actual = CalcPrefix._stack[0]

    # Verify
    assert actual == desired
    # Cleanup - none necessary