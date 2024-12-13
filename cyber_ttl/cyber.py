from .modbus import readHoldingRegisters, readInputRegisters
from .maps.error import error_map

# Function to calculate gas concentration
def calculate_concentration():
    try:
        # Read input registers (sensor reading)
        reg_2000 = readHoldingRegisters(0x00, 1)[0]  # Offset 0x02 from 0x1000

        # Read Real_FS scaling factor
        reg_2007h = readHoldingRegisters(0x07, 1)[0] >> 8  # Offset 0x07 from 0x2000

        # Read holding registers (full scale value)
        reg_1002 = readInputRegisters(0x02, 1)[0]  # Offset 0x00 from 0x2000

        print(f'reg_2000: {reg_2000}, reg_2007h: {reg_2007h}, reg_1002: {reg_2000}')


        # Calculate gas concentration in ppm
        concentration = (reg_1002 * ((round((reg_2000*418)/4096))/10**reg_2007h)) / 418
        return concentration
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_gas_name(sensor_hex, gas_hex):
   
    # Read input registers (sensor reading)
    reg_2000 = readHoldingRegisters(0x00, 1)[0]  # Offset 0x02 from 0x1000

    # Read Real_FS scaling factor
    reg_2007h = readHoldingRegisters(0x07, 1)[0] >> 8  # Offset 0x07 from 0x2000

    
    sensor_name = SENSOR_TYPE_MAP.get(sensor_hex, f"Unknown Sensor (0x{sensor_hex:X})")
    gas_name = GAS_TYPE_MAP.get(gas_hex, f"Unknown Gas (0x{gas_hex:X})")
    
    return f"Sensor: {sensor_name}, Gas: {gas_name}"

def get_error_state():
    try:
        # Read the error register (high byte of register 0x1003)
        error_code = readHoldingRegisters(0x03, 1)[0] >> 8  # Offset 0x03 from 0x1000, and shift to get the high byte

        # Get the error message from the error map, default to UNKNOWN_ERROR if not found
        error_message = error_map.get(error_code, ErrorCode.UNKNOWN_ERROR).value

        # Print the error code and corresponding message
        print(f"Error code: {error_code}, Error message: {error_message}")

        return error_message

    except Exception as e:
        print(f"Error: {e}")
        return None

