# EV BMS Test Simulation

---

## Overview

This project simulates a Battery Management System (BMS) for Electric Vehicles.  
It monitors 6 battery cells for voltage, State of Charge (SOC), and temperature, detects unsafe conditions, and verifies safety logic using automated tests.  
The simulation is modular and can be extended to larger battery packs or integrated with hardware-in-the-loop (HIL) systems.

---

## Features

- Simulates **6 battery cells** with:
  - Voltage (V)
  - State of Charge (SOC, %)
  - Temperature (°C)
- Detects unsafe conditions:
  - Overvoltage / Undervoltage
  - Low SOC
  - Overtemperature
- Includes **automated tests** using **pytest**
- Visualizes battery cell voltages over time using **matplotlib**
- Modular code for easy extension to **larger battery packs** or **HIL systems**

---

## Architecture

Battery Cell Simulation  
↓  
BMS Controller (Safety Logic)  
↓  
Python Simulation Scripts  
↓  
Matplotlib Visualization / Test Reports

---

## Author
Aditya Dipak Chavan