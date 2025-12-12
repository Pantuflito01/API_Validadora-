"""
Custom validation helpers for user data.

These helpers are small utilities used by examples and documentation.
They are not required by the Pydantic `UsuarioValidation` model which
implements its own field validators.
"""

import re
from typing import Tuple, Dict


def validate_email(email: str) -> Tuple[bool, str]:
    """
    Validate an email string using a simple regex.

    Args:
        email: the email string to validate

    Returns:
        Tuple of (is_valid, error_message). `error_message` is empty on success.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True, ""
    return False, "Invalid email format"


def capitalize_name(name: str) -> str:
    """
    Capitalize the first letter and lowercase the rest, trimming whitespace.

    Args:
        name: raw name string

    Returns:
        Normalized name string
    """
    return name.strip().capitalize()


def count_validation_errors(errors: Dict) -> int:
    """
    Count the number of fields that have validation errors.

    Args:
        errors: dictionary mapping field -> error info

    Returns:
        Integer count of keys in `errors`.
    """
    return len(errors)
