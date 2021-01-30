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
        self._operands = {
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
        prefix_expression = self._split_and_reverse_expression(prefix_expression)
        print(prefix_expression)
        for element in prefix_expression:
            
            if element not in self._operands:
                self._stack.append(element)
            else:
                pass

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