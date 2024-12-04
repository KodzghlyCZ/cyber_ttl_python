import serial
import struct

# Constants
FUNCTION_CODE_HOLDING = 0x03
FUNCTION_CODE_INPUT = 0x04
SLAVE_ID = 0x00
PORT = '/dev/ttyCH9344USB0'
BAUD_RATE = 9600
TIMEOUT = 1
INPUT_REGISTER_BASE = 0x1000
HOLDING_REGISTER_BASE = 0x2000

# Global serial connection
serial_connection = None

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

    request_frame = create_modbus_request(SLAVE_ID, function_code, start_addr, num_registers)

    # Log the request frame for debugging
    print(f"Request Frame (hex): {request_frame.hex()}")

    # Send the request frame
    serial_connection.write(request_frame)

    # Wait for the response
    response = serial_connection.read(5 + num_registers * 2)  # Function code, data, CRC

    # Log the response for debugging
    print(f"Response Frame (hex): {response.hex()}")

    return response

# Function to parse a Modbus response frame and extract register values
def parse_modbus_response(response, num_registers):
    if len(response) >= 5 + num_registers * 2:
        data = response[3:-2]  # Exclude slave ID, function code, and CRC
        registers = [struct.unpack('>H', data[i:i+2])[0] for i in range(0, len(data), 2)]
        return registers
    else:
        raise Exception("Invalid response or timeout")

# General function to extract registers from the response
def extract_registers(function_code, start_addr, num_registers):
    response = send_modbus_request(function_code, start_addr, num_registers)
    return parse_modbus_response(response, num_registers)

# Function to read input registers (function code 0x04)
def readInputRegisters(offset, num_registers):
    start_address = INPUT_REGISTER_BASE + offset
    return extract_registers(FUNCTION_CODE_INPUT, start_address, num_registers)

# Function to read holding registers (function code 0x03)
def readHoldingRegisters(offset, num_registers):
    start_address = HOLDING_REGISTER_BASE + offset
    return extract_registers(FUNCTION_CODE_HOLDING, start_address, num_registers)
