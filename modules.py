from typing import Union


def my_adder(a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> Union[int, float]:
    """
    Calculate the sum of three numbers.

    Args:
        a (Union[int, float]): The first number.
        b (Union[int, float]): The second number.
        c (Union[int, float]): The third number.

    Returns:
        Union[int, float]: The sum of a, b, and c.
    """
    out = a + b + c
    return out


def area_of_rectangle(width: Union[int, float], height: Union[int, float]) -> Union[int, float]:
    """
    Calculate the area of a rectangle.

    Args:
        width (Union[int, float]): The width of the rectangle.
        height (Union[int, float]): The height of the rectangle.

    Returns:
        Union[int, float]: The calculated area (width * height).
    """
    return width * height


def have_digits(s: str) -> bool:
    """
    Check if a string contains at least one digit.

    Args:
        s (str): The input string to be checked.

    Returns:
        bool: True if the string contains at least one digit, False otherwise.
    """
    for c in s:
        if c.isdigit():
            return True
    return False


def perimeter_of_rectangle(width: Union[int, float], height: Union[int, float]) -> Union[int, float]:
    """
    Calculate the perimeter of a rectangle.

    Args:
        width (Union[int, float]): The width of the rectangle.
        height (Union[int, float]): The height of the rectangle.

    Returns:
        Union[int, float]: The calculated perimeter (2 * (width + height)).
    """
    return 2 * (width + height)


def my_thermo_stat(temp: int, desired_temp: int) -> str:
    """
    Determine the thermostat status based on the current temperature and desired temperature.

    Args:
        temp (int): The current temperature.
        desired_temp (int): The desired temperature.

    Returns:
        str: The thermostat status, which can be 'Heat', 'AC', or 'off'.
    """
    if temp < desired_temp - 5:
        status = 'Heat'
    elif temp > desired_temp + 5:
        status = 'AC'
    else:
        status = 'off'
    return status
