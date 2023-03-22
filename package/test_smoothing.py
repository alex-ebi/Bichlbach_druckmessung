from pathlib import Path
import util_io
import matplotlib.pyplot as plt


def main():
    messungs_datei = Path("D:\\Baumessungen\\Durchlass_Bichlbach\\messungen_03_06_2022\\Zug9.XLSB")
    df = util_io.rd_messungen_03_06_2022(messungs_datei)
    print(df)

    df_sm = df.rolling(window=30, center=True).mean()

    plt.plot(df['Gleis [Pa]'], 'r--')
    plt.plot(df_sm['Gleis [Pa]'])
    plt.show()


if __name__ == '__main__':
    main()
