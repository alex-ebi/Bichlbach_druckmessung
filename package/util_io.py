import pandas as pd


def rd_messungen(file_path: str, return_header=False) -> pd.DataFrame:
    """
    Liest Excel file von Messungen und gibt sie als np.array aus.

    Parameters
    ----------
    file_path : Dateipfad als string.
    return_header : default False; Wenn True, wird zusätzlich ein Header mit optionaler Information ausgegeben.

    Returns
    -------
    Messungs-df : pd.DataFrame mit Messwerten:
        Spalte 0: Zeit,
        Spalte 1: Druck Wand,
        Spalte 2: Temp Wand,
        Spalte 3: Druck Gleis,
        Spalte 4: Temp Gleis.

    """
    df = pd.read_excel(file_path, index_col=0)
    return df


def rd_messungen_03_06_2022(file_path, return_header=False) -> pd.DataFrame:
    """
    Liest Excel file von Messungen und gibt sie als np.array aus.

    Parameters
    ----------
    file_path :
        Dateipfad als string.
    return_header : default False; Wenn True, wird zusätzlich ein Header mit optionaler Information ausgegeben.

    Returns
    -------
    Messungs-df : pd.DataFrame mit Messwerten:
        Spalte 0: Zeit,
        Spalte 1: Druck Wand,
        Spalte 2: Temp Wand,
        Spalte 3: Druck Gleis,
        Spalte 4: Temp Gleis.

    """
    col_names = ['Wand [Pa]', 'Wand Temp [Ohm]', 'Gleis [Pa]', 'Gleis Temp [Ohm]']
    df = pd.read_excel(file_path, index_col=0, engine='pyxlsb', skiprows=49, header=None, names=col_names)
    return df
