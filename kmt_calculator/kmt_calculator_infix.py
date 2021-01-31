#!/usr/bin/env python3
# -*- coding: latin-1 -*-

import operator
from kmt_calculator.utils import Logging
from kmt_calculator import CalculatorPrefix

""" Calculator to process infix notation (e.g ( 1 + ( 2 * 3 ) ))
"""


class CalculatorInfix(CalculatorPrefix):
    def __init__(self, logger_level: str = "INFO") -> None:
        self._logger = Logging().create_logger(logger_name="CalculatorInfix", logger_level=logger_level)
        self._logger.info("Initialise Infix Calculator")
        self._stack = []
        self._operator_stack = []
        self._operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.floordiv,
        }

    def convert_infix_to_prefix(self, infix_expression: str) -> str:

        for element in infix_expression.split(" "):
            print(element)
            if element == "(":
                self._operator_stack.append(element)
            elif element == ")":
                pass # Add logic later
            elif element in self._operators:
                self._operator_stack.append(element)
            else:
                self._stack.append(element)
                self._apply_operation_no_parenthesis()


    def _apply_operation_no_parentheses(self) -> None:
        if len(self._stack) == 2 and "(" not in self._operator_stack:
            element_2 = self._stack.pop()
            element_1 = self._stack.pop()
            operator = self._operator_stack.pop()
            self._stack.append(f"{operator} {element_1} {element_2}") 
