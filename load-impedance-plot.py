import matplotlib.pyplot as plt
import pandas as pd

FILE = "data/impedance-measurements/Bass_abs_Z.csv"
TIME_COL = 0
DATA_COL = 1
FIG_SIZE = 18


def get_data_from_xlsx(filename: str, x_col, y_col):
    data = pd.read_excel(filename, sheet_name=0)
    x = data.iloc[:, x_col]
    y = data.iloc[:, y_col]
    return x, y


LABEL = "|Z| Bass"

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, layout='constrained', figsize=(FIG_SIZE, FIG_SIZE/3))

# BASS PLOT
f1, z1 = get_data_from_xlsx("data/impedance-measurements/Bass_abs_Z.xlsx", TIME_COL, DATA_COL)
ax1.semilogx(f1, z1, label=LABEL)
ax1.set_xlim(f1.min(), f1.max())
ax1.set_xlabel("f (Hz)")
ax1.set_ylabel("|Z| (Ohm)")
ax1.axvline(x=100, linewidth=0.5, color="red", label="axvline - full height")
ax1.grid(True, which="major", linestyle="-", linewidth=0.8, color="gray")
ax1.grid(True, which="minor", linestyle=":", linewidth=0.5, color="lightgray")
ax1.legend()


# BASS PLOT
f2, z2 = get_data_from_xlsx("data/impedance-measurements/Mid_abs_Z.xlsx", TIME_COL, DATA_COL)
ax2.semilogx(f2, z2, label=LABEL)
ax2.set_xlim(f2.min(), f2.max())
ax2.set_xlabel("f (Hz)")
ax2.set_ylabel("|Z| (Ohm)")
ax2.grid(True)
ax2.legend()


# BASS PLOT
f3, z3 = get_data_from_xlsx("data/impedance-measurements/High_abs_Z.xlsx", TIME_COL, DATA_COL)
ax3.semilogx(f3, z3, label=LABEL)
ax3.set_xlim(f3.min(), f3.max())
ax3.set_xlabel("f (Hz)")
ax3.set_ylabel("|Z| (Ohm)")
ax3.grid(True)
ax3.legend()

# FINAL
plt.show()
