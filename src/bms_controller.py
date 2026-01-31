from battery_cell import BatteryCell

class BMS:
    def __init__(self, cells):
        self.cells = cells  # List of BatteryCell objects

    def check_safety(self):
        warnings = []
        for idx, cell in enumerate(self.cells):
            if cell.voltage < 3.0:
                warnings.append(f"Cell {idx+1} undervoltage: {cell.voltage:.2f}V")
            if cell.voltage > 4.2:
                warnings.append(f"Cell {idx+1} overvoltage: {cell.voltage:.2f}V")
            if cell.temperature > 60:
                warnings.append(f"Cell {idx+1} overtemperature: {cell.temperature:.2f}°C")
            if cell.soc < 5:
                warnings.append(f"Cell {idx+1} SOC low: {cell.soc:.2f}%")
        return warnings

    def balance_cells(self):
        """
        Simple passive balancing: reduce voltage of highest SOC cell by 0.5%
        """
        max_cell = max(self.cells, key=lambda c: c.soc)
        if max_cell.soc > 95:
            max_cell.soc -= 0.5
