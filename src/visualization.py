import matplotlib.pyplot as plt
from battery_cell import BatteryCell

cells = [BatteryCell() for _ in range(6)]
time = []
voltages = [[] for _ in range(6)]

for t in range(50):
    for i, cell in enumerate(cells):
        cell.update(current_draw=2)
        voltages[i].append(cell.voltage)
    time.append(t)

for i in range(6):
    plt.plot(time, voltages[i], label=f'Cell {i+1}')
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Battery Cell Voltages Over Time")
plt.legend()
plt.show()
