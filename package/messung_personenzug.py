"""
Analyse der Messungen von den Zugüberfahrten
"""
import plotting
from einbau import collect_file_paths
import util_io
from matplotlib import pyplot as plt


def main():
    messungs_ordner = "D:\\Baumessungen\\Durchlass_Bichlbach\\messungen_personenzug\\"
    file_paths = collect_file_paths(messungs_ordner)

    print(file_paths)
    for file_path in file_paths:
        df = util_io.rd_messungen(file_path)
        print(file_path)
        print('Maximal, Gleis: ', max(df['Gleis [Pa]'])/1000)
        print('Maximal, Wand: ', max(df['Wand [Pa]'])/1000)
        print('Gleis/Wand: ',  max(df['Gleis [Pa]'])/max(df['Wand [Pa]']))
        f, ax1, ax2 = plotting.plot_2_values(df.index, df['Wand [Pa]'] / 1000, df['Gleis [Pa]'] / 1000, figsize=[10, 3])
        ax1.set_ylabel('p (Wand) (kPa)')
        ax2.set_ylabel('p (Gleis) (kPa)')
        ax1.set_xlabel('t (s)')
        plt.tight_layout(True)
    plt.show()


if __name__ == '__main__':
    main()
