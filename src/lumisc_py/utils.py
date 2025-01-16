"""
Provides useful utilities.
"""

from datetime import date, datetime


def is_date(x) -> bool:
    """
    Check if the given object is a date or datetime object.

    Check if the given object is a date or datetime object.

    Parameters
    ----------
    x : object
        The object to check.

    Returns
    -------
    bool
        True if the object is a date or datetime object, False otherwise.
    """
    return isinstance(x, (date, datetime))
