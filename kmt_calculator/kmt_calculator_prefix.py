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