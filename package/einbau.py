import util_io
import plotting
import os
import numpy as np
from matplotlib import pyplot as plt
import functions


def collect_file_paths(parent_folder: str) -> np.array:
    file_list = os.listdir(parent_folder)

    for i in range(len(file_list)):
        file_list[i] = parent_folder + file_list[i]

    return file_list


def main():
    messungs_ordner = "D:\\Baumessungen\\Durchlass_Bichlbach\\messungen_einbau\\"
    file_paths = collect_file_paths(messungs_ordner)

    for file_path in file_paths[-4:]:
        df = util_io.rd_messungen(file_path)
        temp = functions.resistance_temp(df["Wand Temp [Ohm]"])
        f, ax1, ax2 = plotting.plot_2_values(df.index, df["Wand [Pa]"] * .001, temp,
                                             y2label=r"T($^\circ$C)", y1label="p(kPa)")
        # f, ax1, ax2 = plotting.plot_2_values(temp, temp, df["Wand [Pa]"], y2label=r"p(Pa)", xlabel=r"T($^\circ$C)",
        # y1label=r"T($^\circ$C)") ax1.plot(df.index, functions.remove_offset(df["Wand [Pa]"],
        # functions.resistance_pressure(temp)), color="tab:green")

        p_init = df["Wand [Pa]"][0] * .001
        p_end = df["Wand [Pa]"].iloc[-1] * .001
        delta_p = p_end - p_init

        delta_t = temp.iloc[-1] - temp.iloc[0]

        plt.figtext(.125, .9, file_path[53:-5] + ": Wand" + r", $\Delta p = %.1f\,$kPa, $\Delta T = %.1f\,^\circ$C" %
                    (delta_p, delta_t))

        plotting.set_temp_interval(ax2)  # , interval_size=3.6)

        plt.show()

        temp = functions.resistance_temp(df["Gleis Temp [Ohm]"])
        f, ax1, ax2 = plotting.plot_2_values(df.index, df["Gleis [Pa]"] * .001, temp,
                                             y2label=r"T($^\circ$C)", y1label="p(kPa)")
        # f, ax1, ax2 = plotting.plot_2_values(temp, temp, df["Gleis [Pa]"], y2label=r"p(Pa)", xlabel=r"T($^\circ$C)",
        # y1label=r"T($^\circ$C)") ax1.plot(df.index, functions.remove_offset(df["Gleis [Pa]"],
        # functions.resistance_pressure(temp)), color="tab:green")

        p_init = df["Gleis [Pa]"][0] * .001
        p_end = df["Gleis [Pa]"].iloc[-1] * .001
        delta_p = p_end - p_init
        delta_t = temp.iloc[-1] - temp.iloc[0]

        plt.figtext(.15, .9, file_path[53:-5] + ": Gleis" + r", $\Delta p = %.1f\,$kPa, $\Delta T = %.1f\,^\circ$C" %
                    (delta_p, delta_t))

        plotting.set_temp_interval(ax2)  # , interval_size=10, y_min=11)

        plt.show()


if __name__ == '__main__':
    main()
