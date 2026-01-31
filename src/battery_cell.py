class BatteryCell:
    def __init__(self, voltage=3.7, soc=100, temperature=25, capacity=2.5):
        self.voltage = voltage  # in volts
        self.soc = soc          # State of Charge in %
        self.temperature = temperature  # Celsius
        self.capacity = capacity  # Ah

    def update(self, current_draw, dt=1):
        """
        Update cell SOC and temperature based on current draw (A) and timestep (s)
        """
        # SOC change: ΔSOC = I * dt / Capacity
        delta_soc = (current_draw * dt) / (self.capacity * 3600) * 100
        self.soc -= delta_soc

        # Simple temperature increase for current draw
        self.temperature += abs(current_draw) * 0.05

        # Voltage drops linearly with SOC
        self.voltage = 3.0 + (self.soc / 100) * (4.2 - 3.0)
