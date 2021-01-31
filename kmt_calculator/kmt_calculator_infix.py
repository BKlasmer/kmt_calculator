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

    def parse_infix_expression(self, infix_expression: str) -> int:

        prefix_expression = self.convert_infix_to_prefix(infix_expression)
        return self.parse_prefix_expression(prefix_expression)

    def convert_infix_to_prefix(self, infix_expression: str) -> str:
        
        self._logger.info(f"Converting: {infix_expression}")
        self._clear_stack()
        for element in infix_expression.split(" "):
            if element == "(":
                self._operator_stack.append(element)
            elif element == ")":
                self._apply_right_parentheses_logic()
            elif element in self._operators:
                self._operator_stack.append(element)
            else:
                self._stack.append(element)
                self._apply_operation_no_parentheses()

        if len(self._stack) == 1:
            self._logger.info(f"Converted: {infix_expression} to {self._stack[0]}")
            return self._stack.pop()


    def _apply_operation_no_parentheses(self) -> None:
        """In case of expressions that include a mixture of parentheses or no parentheses (e.g 1 + 2):
        Check if the stack contains at least two elements and that the operator stack has no open
        parenthesis, if so then apply the operator onto the stack.
        """
        if len(self._stack) >= 2 and "(" not in self._operator_stack:
            self._apply_operation()

    def _apply_operation(self) -> None:
        """Pop the 2 last elements in the stack and the last element in the operator stack,
        re-write them in prefix notation and append to the stack.
        """
        element_2 = self._stack.pop()
        element_1 = self._stack.pop()
        operator = self._operator_stack.pop()
        self._stack.append(f"{operator} {element_1} {element_2}")

    def _apply_right_parentheses_logic(self) -> None:

        if "(" not in self._operator_stack:
            self._logger.error("Incorrect infix expression - no open parenthesis before closed parenthesis")
        else:
            self._apply_operation()
            if self._operator_stack[-1] == "(":
                self._operator_stack.pop()
            else:
                self._logger.error("Expecting two arguments in parenthesis (e.g (1 * 2)) not more (e.g (1 * 2 * 3)")
