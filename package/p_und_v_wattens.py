"""
Comparing velocity and maximal pressure.
"""
import paths
import matplotlib.pyplot as plt
import pandas as pd


file = paths.wattens_path / 'geschwindigkeit_und_p_max.xlsx'

df = pd.read_excel(file, header=[0, 1], index_col=0)

print(df.columns)

df = df.drop(2)  # Gueterzug auslassen

plt.scatter(df.loc[:, ('Geschwindigkeit', 'km/h')], df.loc[:, ('pmax(Gleis)', 'kPa')])
plt.xlabel('v (km/h)')
plt.ylabel(r'$p_{max}$ (kPa)')
plt.savefig(paths.wattens_path / 'p_v_wattens.png')
plt.show()