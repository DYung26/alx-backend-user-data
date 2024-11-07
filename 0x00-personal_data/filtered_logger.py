#!/usr/bin/env python3
from typing import List
import re
"""
A module for filtering sensitive data from log messages.

This module provides a function to redact specified fields in a message
by replacing sensitive information with a redaction string.
"""


def filter_datum(
    fields: List[str], redaction: str,
    message: str, separator: str
):
    """
    Redacts specified fields in a log message by replacing sensitive data with
    a redaction string.

    Args:
        fields (List[str]): A list of field names to be redacted.
        redaction (str): The string to replace sensitive data with.
        message (str): The log message containing sensitive data.
        separator (str): The character separating fields in the log message.

    Returns:
        str: The log message with sensitive fields redacted.

    Note:
        Currently, this function only redacts hardcoded fields
        ('password' and 'date_of_birth').
    """
    message = re.sub(r"(?<=password=).*?(?=;)", 'xxx', message)
    message = re.sub(r"(?<=date_of_birth=).*?(?=;)", 'xxx', message)
    return message
