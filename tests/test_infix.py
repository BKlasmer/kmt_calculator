#!/usr/bin/env python3

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
    desired = ["+ 1 2"]

    # Exercise
    CalcInfix = CalculatorInfix()
    CalcInfix._stack = ["1", "2"]
    CalcInfix._operator_stack = ["+"]
    CalcInfix._apply_operation_no_parentheses()
    actual = CalcInfix._stack

    # Verify
    assert actual == desired
    # Cleanup - none necessary


def test_apply_right_parentheses_logic():
    # Setup
    desired_stack = ["+ 1 2"]
    desired_operator_stack = []

    # Exercise
    CalcInfix = CalculatorInfix()
    CalcInfix._stack = ["1", "2"]
    CalcInfix._operator_stack = ["(", "+"]
    CalcInfix._apply_right_parentheses_logic()
    actual_stack = CalcInfix._stack
    actual_operator_stack = CalcInfix._operator_stack

    # Verify
    assert actual_stack == desired_stack
    assert actual_operator_stack == desired_operator_stack
    # Cleanup - none necessary


def test_parse_infix_expression():
    # Setup
    desired = [3, 7, 5, -2]

    # Exercise
    expressions = ["( 1 + 2 )", "( 1 + ( 2 * 3 ) )", "( ( 1 * 2 ) + 3 )", "( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )"]
    CalcInfix = CalculatorInfix()
    actual = [CalcInfix.parse_infix_expression(expression) for expression in expressions]

    # Verify
    assert all([a == b for a, b in zip(actual, desired)])
    # Cleanup - none necessary
