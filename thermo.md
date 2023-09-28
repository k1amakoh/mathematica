# `my_thermo_stat` Function

This page documents the `my_thermo_stat` function, which changes the status of a thermostat based on temperature and desired temperature.


```python
def my_thermo_stat(temp, desired_temp):
    """
    Change the status of the thermostat based on temperature and desired temperature.

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
