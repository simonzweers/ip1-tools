import matplotlib.pyplot as plt
import pandas as pd

FILE = "data/ALL0001/F0001CH1.CSV"
data = pd.read_csv(FILE)
TIME_COL = 3
DATA_COL = 4
LABEL = data.iloc[5,1]
x = data.iloc[:, TIME_COL]
y = data.iloc[:, DATA_COL]

fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x, y, label=LABEL)
ax.set_xlim(x.min(), x.max())
ax.set_xlabel("Time (s)")
ax.set_ylabel("Voltage (V)")
ax.grid(True)
ax.legend()

plt.show()

