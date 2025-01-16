r"""
Provides useful utilities.
"""

from datetime import date, datetime
import numpy as np
import os
import sys


def create_dir(name):
    r"""
    Create a directory if it does not exist.

    If supplied a filepath with multiple directories,
    this function will create all parent directories recursively.

    Parameters
    ----------
    name : str
        Name of the directory to create.
    """
    if not os.path.exists(name):
        os.makedirs(name, exist_ok=True)


def is_date(x) -> bool:
    r"""
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


def nin(x, table):
    r"""
    Inverse value matching.

    Complement of Python's `in` operator. Returns the elements of `x` that are
    not in `table`.

    Parameters
    ----------
    x : array-like
        The values to be matched.
    table : array-like
        The values to be matched against.

    Returns
    -------
    bool
        True for elements of `x` that are not in `table`, False otherwise.
    """
    return ~np.isin(x, table)


def q(*args, **kwargs):
    r"""
    Quit the Python interpreter.

    Parameters
    ----------
    *args :
        Additional arguments passed to `sys.exit()`.
    **kwargs :
        Additional keyword arguments passed to `sys.exit()`.

    Raises
    ------
    SystemExit
        Always raises SystemExit to exit the interpreter.
    """
    sys.exit()
