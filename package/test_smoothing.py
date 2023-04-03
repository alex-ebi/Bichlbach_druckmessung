from pathlib import Path
import util_io
import matplotlib.pyplot as plt
import matplotlib as mpl


def main():
    messungs_datei = Path("D:\\Baumessungen\\Durchlass_Bichlbach\\messungen_03_06_2022\\Zug9.XLSB")
    df = util_io.rd_messungen_03_06_2022(messungs_datei)
    print(df)

    df_sm = df.rolling(window=30, center=True).mean()
    mpl.rcParams.update({'font.size': 15})

    plt.plot(df['Gleis [Pa]'] * .001, 'r--')
    plt.plot(df_sm['Gleis [Pa]'] * .001, 'k')
    plt.ylabel('p (kPa)')
    plt.xlabel('t (s)')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
