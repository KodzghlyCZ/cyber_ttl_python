import serial
import struct

# Constants
FUNCTION_CODE_HOLDING = 0x03
FUNCTION_CODE_INPUT = 0x04
SLAVE_ID = 0x00
BAUD_RATE = 9600
TIMEOUT = 1
INPUT_REGISTER_BASE = 0x1000
HOLDING_REGISTER_BASE = 0x2000

# Global serial connection
serial_connection = None


def open_serial_connection(PORT):
    global serial_connection
    if serial_connection is None:
        serial_connection = serial.Serial(
            PORT, baudrate=BAUD_RATE, timeout=TIMEOUT)
        print("Serial connection opened")
    else:
        print("Serial connection is already open")


def close_serial_connection():
    global serial_connection
    if serial_connection is not None:
        serial_connection.close()
        serial_connection = None
        print("Serial connection closed")
    else:
        print("Serial connection is already closed")

# Function to calculate CRC16 (Modbus RTU CRC)


def calculate_crc16(data):
    crc = 0xFFFF
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x0001:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1
    return struct.pack('<H', crc)

# Function to create a Modbus request frame


def create_modbus_request(slave_id, function_code, start_addr, num_registers):
    request_frame = struct.pack('>B', slave_id)  # Slave ID
    request_frame += struct.pack('>B', function_code)  # Function code
    request_frame += struct.pack('>H', start_addr)  # Starting register address
    request_frame += struct.pack('>H', num_registers)  # Number of registers
    request_frame += calculate_crc16(request_frame)  # CRC16 checksum
    return request_frame

# Function to send a Modbus request and read the response


def send_modbus_request(function_code, start_addr, num_registers):
    global serial_connection
    if serial_connection is None:
        raise Exception("Serial connection is not open")

    request_frame = create_modbus_request(
        SLAVE_ID, function_code, start_addr, num_registers)

    # Log the request frame for debugging
    print(f"Request Frame (hex): {request_frame.hex()}")

    # Send the request frame
    serial_connection.write(request_frame)

    # Wait for the response
    response = serial_connection.read(
        5 + num_registers * 2)  # Function code, data, CRC

    # Log the response for debugging
    print(f"Response Frame (hex): {response.hex()}")

    return response

# Function to parse a Modbus response frame and extract register values


import struct

def parse_modbus_response(response, num_registers, force_array=False):
    if len(response) >= 5 + num_registers * 2:
        # Extract data by excluding slave ID, function code, and CRC
        data = response[3:-2]
        
        # Parse the response into an array of register values
        result = [
            struct.unpack('>H', data[i:i+2])[0]
            for i in range(0, len(data), 2)
        ]

        # If there's only one item, return it unless force_array is True
        if not force_array and len(result) == 1:
            return result[0]
        
        return result  # Return the array for multiple registers or if force_array is True
    else:
        raise ValueError("Response length is insufficient for the given number of registers.")


# General function to extract registers from the response


def extract_registers(function_code, start_addr, num_registers):
    response = send_modbus_request(function_code, start_addr, num_registers)
    return parse_modbus_response(response, num_registers)

# Function to read input registers (function code 0x04)


def readInputRegisters(offset, num_registers=1):
    start_address = INPUT_REGISTER_BASE + offset
    return extract_registers(FUNCTION_CODE_INPUT, start_address, num_registers)

# Function to read holding registers (function code 0x03)


def readHoldingRegisters(offset, num_registers=1):
    start_address = HOLDING_REGISTER_BASE + offset
    return extract_registers(FUNCTION_CODE_HOLDING, start_address, num_registers)
