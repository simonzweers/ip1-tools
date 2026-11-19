import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

FILE = "data/impedance-measurements/Bass_abs_Z.csv"
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
    index = f[index_lower + np.argmax(z[index_lower:index_higher])]
    return index


def get_halfpower_frequencies(z, f, f_peak):
    f_peak_index = np.argwhere(f == f_peak)[0][0]
    print(f_peak_index)
    z_halfpower = z[f_peak_index] / np.sqrt(2)
    delta_z = np.abs(z - z_halfpower)

    # Get first frequency
    i1 = int(np.argmin(delta_z[:f_peak_index]))
    f_1 = f[i1]
    print("First frequency", f_1)


    #Get second frequency
    post_peak_min = np.argmin(z[f_peak_index:]) + f_peak_index
    i2 = int(np.argmin(delta_z[f_peak_index:post_peak_min])) + f_peak_index
    f_2 = f[i2]
    print("Second frequency", f_2)

    # indecies np.where(z=)
    return f_1, f_2


# LABEL = "|Z| Bass"

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, layout='constrained', figsize=(FIG_SIZE, FIG_SIZE/3))

# BASS PLOT
f1, z1 = get_data_from_xlsx("data/impedance-measurements/Bass_abs_Z.xlsx", TIME_COL, DATA_COL)
print("BASS VALUES")
print(f1)
print(len(f1))
print(z1)
label_1 = "Bass"
ax1.set_title(label_1)
ax1.semilogx(f1, z1, label="|Z|")
ax1.set_xlim(f1.min(), f1.max())
ax1.set_xlabel("f (Hz)")
ax1.set_ylabel("|Z| (Ohm)")
f1_peak = get_peak_location(z1, f1, 30, 500)
ax1.axvline(x=f1_peak, linewidth=0.5, color="red", label=f"Peak frequency: {f1_peak}Hz")
f1a, f1b = get_halfpower_frequencies(z1, f1, f1_peak)
ax1.axvline(x=f1a, linewidth=0.5, color="green", label=f"Half-power frequency 1: {f1a}Hz")
ax1.axvline(x=f1b, linewidth=0.5, color="green", label=f"Half-power frequency 2: {f1b}Hz")
ax1.grid(True, which="major", linestyle="-", linewidth=0.8, color="gray")
ax1.grid(True, which="minor", linestyle=":", linewidth=0.5, color="lightgray")
ax1.legend()


# MID PLOT
f2, z2 = get_data_from_xlsx("data/impedance-measurements/Mid_abs_Z.xlsx", TIME_COL, DATA_COL)
print("MID VALUES")
print(f2)
print(z2)
label_2 = "Midtones"
ax2.semilogx(f2, z2, label="|Z|")
ax2.set_xlim(f2.min(), f2.max())
ax2.set_xlabel("f (Hz)")
ax2.set_ylabel("|Z| (Ohm)")
f2_peak = get_peak_location(z2, f2, 30, 500)
ax2.axvline(x=f2_peak, linewidth=0.5, color="red", label=f"Peak frequency: {f2_peak}Hz")
f2a, f2b = get_halfpower_frequencies(z2, f2, f2_peak)
ax2.axvline(x=f2a, linewidth=0.5, color="green", label=f"Half-power frequency 1: {f2a}Hz")
ax2.axvline(x=f2b, linewidth=0.5, color="green", label=f"Half-power frequency 2: {f2b}Hz")
ax2.grid(True, which="major", linestyle="-", linewidth=0.8, color="gray")
ax2.grid(True, which="minor", linestyle=":", linewidth=0.5, color="lightgray")
ax2.legend()


# HIGH PLOT
f3, z3 = get_data_from_xlsx("data/impedance-measurements/High_abs_Z.xlsx", TIME_COL, DATA_COL)
print("HIGH VALUES")
print(f3)
print(z3)
label_3 = "High"
ax3.semilogx(f3, z3, label="|Z|")
ax3.set_xlim(f3.min(), f3.max())
ax3.set_xlabel("f (Hz)")
ax3.set_ylabel("|Z| (Ohm)")
f3_peak = get_peak_location(z3, f3, 100, 5000)
ax3.axvline(x=f3_peak, linewidth=0.5, color="red", label=f"Peak frequency: {f3_peak}Hz")
f3a, f3b = get_halfpower_frequencies(z3, f3, f3_peak)
ax3.axvline(x=f3a, linewidth=0.5, color="green", label=f"Half-power frequency 1: {f3a}Hz")
ax3.axvline(x=f3b, linewidth=0.5, color="green", label=f"Half-power frequency 2: {f3b}Hz")
ax3.grid(True, which="major", linestyle="-", linewidth=0.8, color="gray")
ax3.grid(True, which="minor", linestyle=":", linewidth=0.5, color="lightgray")
ax3.legend()

# FINAL
plt.show()
