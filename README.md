# My Modbus Package

This package provides functionality for Modbus communication over a serial connection and calculates gas concentration based on sensor readings.

## Installation

You can install the package using pip:

```
pip install my_modbus_package
```

## Usage

```python
from my_modbus_package import open_serial_connection, close_serial_connection, calculate_concentration

# Open serial connection
open_serial_connection()

# Calculate gas concentration
concentration = calculate_concentration()
print(f"Gas Concentration: {concentration:.2f} ppm")

# Close serial connection
close_serial_connection()
```

## Dependencies

- pyserial
- pymodbus
