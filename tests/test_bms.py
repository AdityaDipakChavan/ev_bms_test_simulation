# tests/test_bms.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from battery_cell import BatteryCell
from bms_controller import BMS

def test_voltage_limits():
    cell = BatteryCell(voltage=4.3)
    bms = BMS([cell])
    warnings = bms.check_safety()
    assert any("overvoltage" in w.lower() for w in warnings)

def test_soc_low():
    cell = BatteryCell(soc=3)
    bms = BMS([cell])
    warnings = bms.check_safety()
    assert any("soc low" in w.lower() for w in warnings)

def test_temperature_limit():
    cell = BatteryCell(temperature=65)
    bms = BMS([cell])
    warnings = bms.check_safety()
    assert any("overtemperature" in w.lower() for w in warnings)
