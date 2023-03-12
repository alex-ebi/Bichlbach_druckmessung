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

        if 'fahrt_20_ibk' in key:
            trigger = df['Gleis [Pa]'][df['Gleis [Pa]'] > 10000].index[0]
            x_range = [-2, 6]
            y2_range = [-1, 40]
            y1_max = 10
            y1_range = [y1_max / ((x_range[1] - x_range[0]) / x_range[0] + 1), y1_max]
            plot_df = df.loc[trigger + x_range[0]:trigger + x_range[1], :]
            x_plot = plot_df.index - trigger
        elif 'fahrt_20_reutte' in key:
            trigger = df['Gleis [Pa]'][df['Gleis [Pa]'] > 10000].index[0]
            x_range = [-3, 5]
            y2_range = [-1, 40]
            y1_max = 10
            plot_df = df.loc[trigger + x_range[0]:trigger + x_range[1], :]
            x_plot = plot_df.index - trigger

        elif 'fahrt_40' in key:
            trigger = df['Gleis [Pa]'][df['Gleis [Pa]'] > 10000].index[0]
            x_range = [-1, 3]
            y2_range = [-1, 40]
            y1_max = 10
            plot_df = df.loc[trigger + x_range[0]:trigger + x_range[1], :]
            x_plot = plot_df.index - trigger

        else:
            x_range = None
            y2_range = None
            plot_df = df
            x_plot = plot_df.index

        y_wand = plot_df.loc[:, 'Wand [Pa]'] - np.min(plot_df.loc[:, 'Wand [Pa]'])
        y_gleis = plot_df.loc[:, 'Gleis [Pa]'] - np.min(plot_df.loc[:, 'Gleis [Pa]'])

        pe_gleis = 22.5
        pe_wand = 9.2

        print('Maximal, Gleis: ', np.nanmax(y_gleis) / 1000 + pe_gleis)
        print('Maximal, Wand: ', np.nanmax(y_wand) / 1000+pe_wand)
        # print('Gleis/Wand: ', np.nanmax(y_gleis) / np.nanmax(y_wand))

        f, ax1, ax2 = plotting.plot_2_values(x_plot, y_wand / 1000, y_gleis / 1000, figsize=[10, 3])
        ax1.set_ylabel('p (Wand) (kPa)')
        ax2.set_ylabel('p (Gleis) (kPa)')
        ax1.set_xlabel('t (s)')
        ax1.set_xlim(x_range)
        # ax1.set_ylim(y1_range)
        # ax2.set_ylim(y2_range)
        f.canvas.manager.set_window_title(f'{key}_zug{messung}')
        plt.tight_layout()
        plt.show()
        # plt.savefig(Path(r"D:\Baumessungen\Durchlass_Bichlbach\messkurven_lok") / f'{key}_zug{messung}.png')
        # plt.close()


def main():
    mess_gruppen = {'fahrt_20_ibk': [8, 14, 22, 28],
                    'fahrt_20_reutte': [7, 15, 21, 29],
                    'fahrt_40_ibk': [2, 10, 16, 24],
                    'fahrt_40_reutte': [1, 9, 17, 23],
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
    for key, mess_gruppe in list(mess_gruppen.items())[-2:]:
        print(key, mess_gruppe)
        for messung in mess_gruppe:
            iter_func(messung, key)


if __name__ == '__main__':
    main()
