"""
Provides text manipulation functions.
"""


def count_lines(filepath, batch_size=1000):
    r"""
    Count the number of lines in a given text file.

    This function counts the lines of a given text file line by line to prevent
    reading the entire file into memory at once. Higher batch sizes generally
    equal quicker read times.

    Parameters
    ----------
    filepath : str
        Path to the text file.
    batch_size : int, optional
        Number of lines to read in at one time. Defaults to 1000.

    Returns
    -------
    int
        Number of lines in the file.
    """
    with open(filepath, "r") as f:
        line_count = 0
        while True:
            lines = f.readlines(batch_size)
            line_count += len(lines)
            if len(lines) < batch_size:
                break
    return line_count
