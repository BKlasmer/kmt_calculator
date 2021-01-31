#!/usr/bin/env python3
# -*- coding: latin-1 -*-

import operator
from kmt_calculator.utils import Logging

""" Calculator to process prefix notation (e.g + * 1 2 3)
"""


class CalculatorPrefix(object):
    def __init__(self, logger_level: str = "INFO") -> None:
        self._logger = Logging().create_logger(logger_name="CalculatorPrefix", logger_level=logger_level)
        self._logger.info("Initialise Prefix Calculator")
        self._stack = []
        self._operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.floordiv,
        }

    def parse_prefix_expression(self, prefix_expression: str) -> int:
        """Parses a space separated prefix expression with the following considerations:

        - The system supports the operators {+, -, *, /} which all take exactly two args.
        - The input literals are positive integers.
        - Calculations can be done in the integer domain.
        - Division by zero isn't handled.
        - Operator presidence isn't evaluated.

        Args:
            prefix_expression (str): A space seperated prefix expression (e.g "- / 10 + 1 1 * 1 2")

        Returns:
            int: The calculation output
        """

        self._logger.info(f"Evaluating: {prefix_expression}")
        self._clear_stack()
        prefix_expression = self._split_and_reverse_expression(prefix_expression)
        for element in prefix_expression:

            if element not in self._operators:
                self._stack.append(int(element))
            else:
                self._perform_prefix_operation(element)

        if len(self._stack) == 1:
            return self._stack.pop()

        else:
            self._logger.error(f"Invalid prefix expression: {prefix_expression}")

    def _perform_prefix_operation(self, operator: str) -> None:
        """Calculates the operation between the last two elements in the stack
        and appends the output to the stack

        Args:
            operator (str): One of "+", "-", "*" or "/"
        """
        operator_function = self._operators[operator]
        element_1 = self._stack.pop()
        element_2 = self._stack.pop()
        self._stack.append(operator_function(element_1, element_2))

    def _clear_stack(self):
        self._stack = []

    @staticmethod
    def _split_and_reverse_expression(prefix_expression: str) -> list:
        """Splits the prefix expression and reverses the order of the elements

        Args:
            prefix_expression (str): A space seperated prefix expression (e.g "- / 10 + 1 1 * 1 2")

        Returns:
            list: List of the elements in the prefix expression in reversed order
        """
        prefix_expression = prefix_expression.split(" ")
        prefix_expression.reverse()
        return prefix_expression
