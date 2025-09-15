"""
Analyse der Messungen von den Zugüberfahrten
"""
import plotting
import util_io
from matplotlib import pyplot as plt
import paths


def main():
    messungs_ordner = paths.wattens_path / 'messungen_zug'
    file_paths = messungs_ordner.glob('*.xlsb')

    for file_path in file_paths:
        df = util_io.rd_messungen_wattens_2024(file_path)
        print(file_path)
        print('Maximal, Gleis: ', max(df['1 [Pa]']) / 1000)
        print('Maximal, Wand: ', max(df['2 [Pa]']) / 1000)
        print('Gleis/Wand: ', max(df['1 [Pa]']) / max(df['2 [Pa]']))
        f, ax1, ax2 = plotting.plot_2_values(df.index, df['1 [Pa]'] / 1000, df['2 [Pa]'] / 1000, figsize=[10, 3])
        ax1.set_ylabel('p (1) (kPa)')
        ax2.set_ylabel('p (2) (kPa)')
        ax1.set_xlabel('t (s)')
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    main()
