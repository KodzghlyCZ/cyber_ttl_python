from .modbus import readHoldingRegisters, readInputRegisters
from .maps.error import error_map
from .maps.sensor_gas_types import sensorGasTypeMap

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

def get_gas_name():
    try:
        # Read sensor and gas registers
        sensor_hex = readHoldingRegisters(0x0E, 1)[0]  # Example address for sensor register
        gas_hex = readHoldingRegisters(0x14, 1)[0]  # Example address for gas register


        # Combine the sensor and gas register values to create a unique key
        combined_key = ((sensor_hex << 8) | (gas_hex >> 8)) & 0xFFFF

        
        # Look up the gas name using the combined key
        gas_name = sensorGasTypeMap.get(combined_key, f"Unknown Gas (0x{combined_key:X})")
        
        # Return the gas name
        return f"Gas: {gas_name}"
    
    except Exception as e:
        print(f"Error: {e}")
        return "Error retrieving gas name"

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

