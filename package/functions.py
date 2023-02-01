import numpy as np
import pandas as pd


def temp_pressure(temp: np.array) -> np.array:
    """
    Linear relation between temperature and pressure.

    pressure = a * temp + b

    Parameters
    ----------
    temp : temperature array

    Returns
    -------
    Pressure array

    """
    a = 4333
    b = -38481

    return a * temp + b


def resistance_pressure(resist: np.array) -> np.array:
    """
    Linear relation between resistance (temperature) and pressure.

    pressure = a * resist + b

    Parameters
    ----------
    resist : resistance (temperature) array

    Returns
    -------
    Pressure array

    """
    a = -15.84
    b = 97466

    return a * resist + b


def resistance_temp(resist: np.array) -> pd.Series:
    """
    Relation zwischen Widerstand-output und tatsächlicher Temperatur.

    Thermistor Type: YSI 44005, Dale #1C3001-B3, Alpha #13A3001-B3
    Parameters
    ----------
    resist : gemessener Widerstand

    Returns
    -------
    Temperature : pd.Series
    """

    # Coefficients
    a = 1.4051e-3
    b = 2.369e-4
    c = 1.1019e-7
    t0 = 273.15  # constant temperature offset in Celsius

    return 1 / (a + b * np.log(resist) + c * np.log(resist) ** 3) - t0


def remove_offset(y1: np.array, y2: np.array) -> np.array:
    offset = np.median(y1 - y2)

    return y2 + offset
