
def percent(part: float, whole: float) -> float:
    """
    Calculates the percentage of 'part' based on 'whole'.

    :param float part: The part value which represents a portion of the whole.
    :param float whole: The whole value against which the part is measured.
    :return: The calculated percentage of the part relative to the whole
    :raises ValueError: If the whole is zero, resulting in division by zero.
    :raises TypeError:  If the inputs are not of type int or float.

    This function employs detailed validation mechanisms and incorporates
    exception handling to ensure that inputs are of the correct type and
    value, providing informative error messages in case of invalid input.

    Example:

    >>> percent(25, 100)
    25.0
    >>> percent(7, 0)
    ValueError: Whole cannot be zero. Division by zero is undefined.
    """
    if not (isinstance(part, (int, float)) and isinstance(whole, (int, float))):
        raise TypeError("Both 'part' and 'whole' must be numbers (int or float).")

    if whole == 0:
        raise ValueError("Whole cannot be zero. Division by zero is undefined.")

    result = (part / whole) * 100

    return result


