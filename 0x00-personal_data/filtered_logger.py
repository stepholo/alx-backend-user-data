#!/usr/bin/env python3
"""Module to define function filter_datum"""


import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """A function called filter_datum that returns
       the log message obfuscated
    """
    return re.sub(r'\b(?:' + '|'.join(fields) + r')\b', redaction, message)
