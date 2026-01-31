from battery_cell import BatteryCell
from bms_controller import BMS

def simulate_scenario(current_draw, steps=100):
    # Create 6 battery cells
    cells = [BatteryCell() for _ in range(6)]
    bms = BMS(cells)

    for t in range(steps):
        for cell in cells:
            cell.update(current_draw)
        warnings = bms.check_safety()
        if warnings:
            print(f"Step {t}: {warnings}")

if __name__ == "__main__":
    print("Normal operation:")
    simulate_scenario(current_draw=1.0)

    print("\nOvercurrent scenario:")
    simulate_scenario(current_draw=20.0)
