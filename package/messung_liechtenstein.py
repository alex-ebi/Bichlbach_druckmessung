"""
Analyse der Messungen von den Zugüberfahrten
"""
import plotting
import util_io
from matplotlib import pyplot as plt
import paths
from astro_scripts_uibk import spectrum_reduction
import numpy as np


def main():
    messungs_ordner = paths.root_path / 'Liechtenstein_2026/Messungen_2026'
    plot_ordner = messungs_ordner / 'plots'
    file_paths = messungs_ordner.glob('*.xlsb')

    for file_path in file_paths:
        print(file_path)
        df = util_io.read_dms(file_path)
        print(file_path)
        # print('Maximal, Gleis: ', max(df['1 [Pa]']) / 1000 + 27.2)
        # print('Maximal, Wand: ', max(df['2 [Pa]']) / 1000 + 3.9)
        # print('Gleis/Wand: ', max(df['1 [Pa]']) / max(df['2 [Pa]']))

        smooth_1 = spectrum_reduction.smooth_spec(np.array([df.index, df['DMS_1 [um/m]']]), 50)
        smooth_2 = spectrum_reduction.smooth_spec(np.array([df.index, df['DMS_2 [um/m]']]), 50)

        f, ax1, ax2 = plotting.plot_2_values(df.index, df['DMS_1 [um/m]'], df['DMS_2 [um/m]'], figsize=[15, 5])
        ax1.set_ylabel('DMS 1 [um/m]')
        ax2.set_ylabel('DMS 2 [um/m]')
        ax1.set_xlabel('t (s)')
        plt.tight_layout()
        plt.savefig(plot_ordner / file_path.name.replace('.xlsb', '.png'))
        plt.close()
        
        f, ax1, ax2 = plotting.plot_2_values(smooth_1[0], smooth_1[1], smooth_2[1], figsize=[15, 5])
        ax1.set_ylabel('DMS 1 [um/m]')
        ax2.set_ylabel('DMS 2 [um/m]')
        ax1.set_xlabel('t (s)')
        plt.tight_layout()
        plt.savefig(plot_ordner / (file_path.name.replace('.xlsb', '') + '_smooth.png'))
        plt.close()
        # plt.show()


if __name__ == '__main__':
    main()
