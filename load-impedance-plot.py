import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

TIME_COL = 0
DATA_COL = 1
FIG_SIZE = 18


def get_data_from_xlsx(filename: str, x_col, y_col):
    data = pd.read_excel(filename, sheet_name=0)
    x = np.array(data.iloc[:, x_col])
    y = np.array(data.iloc[:, y_col])
    return x, y


def get_peak_location(z, f, limit_lower, limit_higher):
    index_lower = int(np.argwhere(f <= limit_lower).flatten()[-1])
    index_higher = int(np.argwhere(f >= limit_higher).flatten()[0])
    index = index_lower + np.argmax(z[index_lower:index_higher])
    f_ret = f[index]
    return f_ret, index


def get_halfpower_frequencies(z, f, f_peak):
    f_peak_index = np.argwhere(f == f_peak)[0][0]
    z_halfpower = z[f_peak_index] / np.sqrt(2)
    delta_z = np.abs(z - z_halfpower)

    # Get first frequency
    i1 = int(np.argmin(delta_z[:f_peak_index]))
    f_1 = f[i1]

    # Get second frequency
    post_peak_min = np.argmin(z[f_peak_index:]) + f_peak_index
    i2 = int(np.argmin(delta_z[f_peak_index:post_peak_min])) + f_peak_index
    f_2 = f[i2]

    # indecies np.where(z=)
    return f_1, f_2


def find_value_index(f, f_find):
    f_index = int(np.argwhere(f >= f_find).flatten()[0])
    return f_index


def plot_z(filename, ax, label_txt, peak_lower, peak_higher):
    # Plot data aquisition, plot settings
    f, z = get_data_from_xlsx(filename, TIME_COL, DATA_COL)
    ax.set_title(label_txt)
    ax.semilogx(f, z, label="|Z|")
    ax.set_xlim(f.min(), f.max())
    ax.set_xlabel("f (Hz)")
    ax.set_ylabel("|Z| (Ohm)")
    ax.grid(True, which="major", linestyle="-", linewidth=0.8, color="gray")
    ax.grid(True, which="minor", linestyle=":", linewidth=0.5, color="lightgray")

    # Peak frequency
    f_peak, f_peak_index = get_peak_location(z, f, peak_lower, peak_higher)
    ax.scatter(f_peak, z[f_peak_index], c='black', marker='.', label=f"{z[f_peak_index]} Ohm", s=30)
    ax.axvline(x=f_peak, linewidth=0.5, color="red", label=f"Peak frequency: {f_peak}Hz")

    # Half power frequencies
    f1a, f1b = get_halfpower_frequencies(z, f, f_peak)
    ax.axvline(x=f1a, linewidth=0.5, color="green", label=f"Half-power frequency 1: {f1a}Hz")
    ax.axvline(x=f1b, linewidth=0.5, color="green", label=f"Half-power frequency 2: {f1b}Hz")

    # Plot dZ/dw
    f_slope_1_index = find_value_index(f, 10000)
    f_slope_2_index = find_value_index(f, 15000)

    dZ_df = (z[f_slope_2_index] - z[f_slope_1_index]) / (f[f_slope_2_index] - f[f_slope_1_index])
    dZ_dw = dZ_df / (np.pi * 2)
    print(f"{label_txt}: dZ/dw = {dZ_dw}, dZ_df = {dZ_df}")

    ax.legend()


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, layout='constrained', figsize=(FIG_SIZE, FIG_SIZE/3))

plot_z("data/impedance-measurements/Bass_abs_Z.xlsx", ax1, "Bass", 30, 500)
plot_z("data/impedance-measurements/Mid_abs_Z.xlsx", ax2, "Midtones", 50, 500)
plot_z("data/impedance-measurements/High_abs_Z.xlsx", ax3, "High", 100, 2000)

# FINAL
plt.show()
