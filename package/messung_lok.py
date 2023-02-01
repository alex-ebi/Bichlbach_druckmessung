"""
Analyse der Messungen von den Zugüberfahrten
"""
import plotting
from einbau import collect_file_paths
import util_io
from matplotlib import pyplot as plt
from pathlib import Path
import pandas as pd
import numpy as np


def iter_func(messung: int, key: str):
    messungs_ordner = Path("D:\\Baumessungen\\Durchlass_Bichlbach\\messungen_03_06_2022\\")
    file_paths = messungs_ordner.glob(f'*Zug{messung}.XLSB')

    for file_path in file_paths:
        print(file_path)
        df = util_io.rd_messungen_03_06_2022(file_path)

        # print('Maximal, Gleis: ', np.nanmax(df['Gleis [Pa]']) / 1000)
        # print('Maximal, Wand: ', np.nanmax(df['Wand [Pa]']) / 1000)
        # print('Gleis/Wand: ', np.nanmax(df['Gleis [Pa]']) / np.nanmax(df['Wand [Pa]']))

        f, ax1, ax2 = plotting.plot_2_values(df.index, df['Wand [Pa]'] / 1000, df['Gleis [Pa]'] / 1000, figsize=[10, 3])
        ax1.set_ylabel('p (Wand) (kPa)')
        ax2.set_ylabel('p (Gleis) (kPa)')
        ax1.set_xlabel('t (s)')
        f.canvas.manager.set_window_title(f'{key}_zug{messung}')
        plt.tight_layout()
        plt.show()


def main():
    mess_gruppen = {'fahrt_20_ibk': [8, 14, 22, 28],
                    'fahrt_20_reutte': [7, 15, 21, 29],
                    'fahrt_40_ibk': [2, 10, 16, 24],
                    'fahrt_40_reutte': [2, 9, 17, 23],
                    'bremsen_ibk_1': [6],
                    'bremsen_ibk_2': [12],
                    'bremsen_ibk_3': [20],
                    'bremsen_ibk_4': [26],
                    'bremsen_reutte_1': [5],
                    'bremsen_reutte_2': [13],
                    'bremsen_reutte_3': [19],
                    'bremsen_reutte_4': [27],
                    'aufstellung_ibk': [18, 30],
                    'aufstellung_reutte': [4, 11, 25]

                    }
    for key, mess_gruppe in mess_gruppen.items():
        print(key, mess_gruppe)
        for messung in mess_gruppe:
            iter_func(messung, key)


if __name__ == '__main__':
    main()
