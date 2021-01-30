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

def test_parse_prefix_expression():
    # Setup
    desired_1 = 3
    desired_2 = 3
    desired_3 = 7
    desired_4 = 5
    desired_5 = 3
    desired_6 = -3
    desired_7 = 1

    # Exercise
    CalcPrefix = CalculatorPrefix()
    actual_1 = CalcPrefix.parse_prefix_expression("3")
    actual_2 = CalcPrefix.parse_prefix_expression("+ 1 2")
    actual_3 = CalcPrefix.parse_prefix_expression("+ 1 * 2 3")
    actual_4 = CalcPrefix.parse_prefix_expression("+ * 1 2 3")
    actual_5 = CalcPrefix.parse_prefix_expression("- / 10 + 1 1 * 1 2")
    actual_6 = CalcPrefix.parse_prefix_expression("- 0 3")
    actual_7 = CalcPrefix.parse_prefix_expression("/ 3 2")

    # Verify
    assert actual_1 == desired_1
    assert actual_2 == desired_2
    assert actual_3 == desired_3
    assert actual_4 == desired_4
    assert actual_5 == desired_5
    assert actual_6 == desired_6
    assert actual_7 == desired_7
    # Cleanup - none necessary