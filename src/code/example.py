# The docstring of this function (""" """" below after def) will automatically go into api.md
# Path is specified in conf.py as '../code'
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    :param a: First number.
    :param b: Second number.
    :return: The product of a and b.
    """
    return a * b