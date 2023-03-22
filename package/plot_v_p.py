from matplotlib import pyplot as plt
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib as mpl

mpl.rcParams.update({'font.size': 15})


def main():
    excel_path = Path("D:\\Baumessungen\\Durchlass_Bichlbach\\analyse_lok\\smoothed_maxima.xlsx")

    df = pd.read_excel(excel_path, index_col=0)

    ind_0 = [item for item in df.index if 'aufstellung' in item]
    ind_20 = [item for item in df.index if '20' in item]
    ind_40 = [item for item in df.index if '40' in item]

    max_0 = df.loc[ind_0, :].max(axis=0)
    max_20 = df.loc[ind_20, :].max(axis=0)
    max_40 = df.loc[ind_40, :].max(axis=0)

    x = np.array([0, 20, 40])
    # y = np.array([max_0['Max.Gleis'], max_20['Max.Gleis'], max_40['Max.Gleis']])
    y = np.array([max_0['Max.Wand'], max_20['Max.Wand'], max_40['Max.Wand']])

    f = np.polyfit(x, y, 1)

    def f_plot(x_f):
        return f[1] + f[0] * x_f

    fig, ax = plt.subplots(figsize=[5, 4.5])
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    plt.xlabel('Geschwindigkeit (km/h)')
    plt.ylabel('Druck (kPa)')
    plt.scatter(x, y, color='k')

    # plt.plot(x, f_plot(x), 'k')
    #
    # ax.text(0.05, 0.95, f'Steigung Fit: {np.round(f[0], 2):.2f} kPa/(km/h)', transform=ax.transAxes, bbox=props,
    #         verticalalignment='top')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
