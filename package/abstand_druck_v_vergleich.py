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
import matplotlib as mpl
import paths

mpl.rcParams.update({'font.size': 15})


def iter_func(messung: int, key: str, ax1, ax2, messungs_ordner, plot=True):
    file_paths = messungs_ordner.glob(f'*Zug{messung}.XLSB')

    for file_path in file_paths:
        print(file_path)
        df = util_io.rd_messungen_03_06_2022(file_path)

        # smoothing
        df = df.rolling(window=30, center=True).mean()
        x_range = [-6, 8]

        if 'fahrt_20_ibk' in key:
            trigger = df['Gleis [Pa]'].idxmax()
            y2_range = [-1, 40]
            y1_max = 10
            y1_range = [y1_max / ((x_range[1] - x_range[0]) / x_range[0] + 1), y1_max]
            plot_df = df.loc[trigger + x_range[0]:trigger + x_range[1], :]
            x_plot = plot_df.index - trigger
            x_plot *= 20.5 / 3.6
        elif 'fahrt_20_reutte' in key:
            trigger = df['Gleis [Pa]'].idxmax()
            y2_range = [-1, 40]
            y1_max = 10
            plot_df = df.loc[trigger + x_range[0]:trigger + x_range[1], :]
            x_plot = plot_df.index - trigger
            x_plot *= 20 / 3.6

        elif 'fahrt_40' in key:
            trigger = df['Gleis [Pa]'].idxmax()
            y2_range = [-1, 40]
            y1_max = 10
            plot_df = df.loc[trigger + x_range[0]:trigger + x_range[1], :]
            x_plot = plot_df.index - trigger
            x_plot *= 40 / 3.6

        else:
            x_range = None
            y2_range = None
            plot_df = df
            x_plot = plot_df.index

        y_wand = plot_df.loc[:, 'Wand [Pa]'] - np.min(plot_df.loc[:, 'Wand [Pa]'])
        y_gleis = plot_df.loc[:, 'Gleis [Pa]'] - np.min(plot_df.loc[:, 'Gleis [Pa]'])

        pe_gleis = 22.5
        pe_wand = 11.7

        max_gleis = np.nanmax(y_gleis) / 1000 + pe_gleis
        max_wand = np.nanmax(y_wand) / 1000 + pe_wand

        print('Maximal, Gleis: ', max_gleis)
        print('Maximal, Wand: ', max_wand)
        # print('Gleis/Wand: ', np.nanmax(y_gleis) / np.nanmax(y_wand))

        if plot:
            mpl.rcParams.update({'font.size': 15})

            # color = "tab:blue"
            # ax1.plot(x_plot, y_wand / 1000, color=color)

            # color = "tab:orange"
            # ax2.plot(x_plot, y_gleis / 1000, color=color)

            if '20' in key:
                linestyle = '--'
            else:
                linestyle = '-'
            ax2.plot(x_plot, y_gleis / 1000, linestyle, label=key)

            ax1.grid(True)

        return [max_gleis, max_wand]


def main():
    messungs_ordner = paths.data_path / "messungen_03_06_2022"

    mess_gruppen = {'fahrt_20_ibk': [8, 14, 22, 28],
                    'fahrt_20_reutte': [7, 15, 21, 29],
                    'fahrt_40_ibk': [2, 10, 16, 24],
                    'fahrt_40_reutte': [1, 9, 17, 23],
                    }
    # mess_gruppen = {'fahrt_20_ibk': [8, 14, 22, 28],
    #                 'fahrt_40_ibk': [2, 10, 16, 24],
    #                 }
    # mess_gruppen = {'fahrt_20_ibk': [8],
    #                 'fahrt_40_ibk': [2],
    #                 }
    max_df = pd.DataFrame()
    f, ax1 = plt.subplots(figsize=[10, 4])
    ax2 = ax1.twinx()
    ax1.set_ylabel('p (Wand) (kPa)')
    ax2.set_ylabel('p (Gleis) (kPa)')
    ax1.set_xlabel('s (m)')

    for key, mess_gruppe in list(mess_gruppen.items()):
        print(key, mess_gruppe)
        max_array = []
        for messung in mess_gruppe:
            max_array.append(iter_func(messung, key, ax1, ax2, messungs_ordner, plot=True))

        max_array = np.array(max_array)
        print('Max Messreihe Gleis und Wand:')
        max_messreihe = np.max(max_array, axis=0)
        s = pd.Series(data=max_messreihe, index=['Max.Gleis', 'Max.Wand'], name=key)

        max_df = pd.concat((max_df, s), axis=1)

    # plt.legend()
    plt.tight_layout()
    plt.show()
    max_df = max_df.T
    max_df.to_excel(paths.data_path / 'analyse_lok/smoothed_maxima.xlsx')
    print(max_df)


if __name__ == '__main__':
    main()
