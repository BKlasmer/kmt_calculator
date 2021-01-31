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
        self._operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.floordiv,
        }