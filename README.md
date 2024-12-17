# Cyber TTL 

This package provides very limited functionality for communication with CYBER TTL boards from n.e.t. . Since I don't have much time to do things the proper way, I'm open to any PRs to help me make the package contain all the features according to the [documentation](https://www.nenvitech.com/wp-content/uploads/2024/05/MT3741_CYBER_MODBUS_CUSTOMER_MANUAL_Rev.-19.pdf)

## Installation

You can install the package using pip:

```
pip install git+https://github.com/KodzghlyCZ/cyber_ttl_python.git
```

## Usage

```python
from cyber_ttl import open_serial_connection, close_serial_connection, calculate_concentration

# Main function
def main():
    try:
        open_serial_connection('/dev/ttyUSB0') #Modify this to fit your needs
        concentration = calculate_concentration()
        if concentration is not None:
            print(f"Gas Concentration: {concentration:.2f} ppm")
    finally:
        close_serial_connection()

if __name__ == "__main__":
    main()

```

## Dependencies

- pyserial
