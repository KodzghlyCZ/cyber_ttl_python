import serial
import serial.rs485
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

def open_serial_connection(PORT, rs485=False):
    global serial_connection
    if serial_connection is None:
        if rs485:
            serial_connection = serial.rs485.RS485(
                port=PORT, baudrate=BAUD_RATE, timeout=TIMEOUT
            )
            serial_connection.rs485_mode = serial.rs485.RS485Settings(
                rts_level_for_tx=True,
                rts_level_for_rx=False,
                delay_before_tx=0.01,
                delay_before_rx=0.01
            )
        else:
            serial_connection = serial.Serial(
                PORT, baudrate=BAUD_RATE, timeout=TIMEOUT
            )
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

def create_modbus_request(slave_id, function_code, start_addr, num_registers):
    request_frame = struct.pack('>B', slave_id)
    request_frame += struct.pack('>B', function_code)
    request_frame += struct.pack('>H', start_addr)
    request_frame += struct.pack('>H', num_registers)
    request_frame += calculate_crc16(request_frame)
    return request_frame

def send_modbus_request(function_code, start_addr, num_registers):
    global serial_connection
    if serial_connection is None:
        raise Exception("Serial connection is not open")

    request_frame = create_modbus_request(SLAVE_ID, function_code, start_addr, num_registers)
    print(f"Request Frame (hex): {request_frame.hex()}")

    serial_connection.write(request_frame)
    response = serial_connection.read(5 + num_registers * 2)
    print(f"Response Frame (hex): {response.hex()}")
    return response

def parse_modbus_response(response, num_registers, force_array=False):
    if len(response) >= 5 + num_registers * 2:
        data = response[3:-2]
        result = [
            struct.unpack('>H', data[i:i+2])[0]
            for i in range(0, len(data), 2)
        ]
        return result if force_array or len(result) > 1 else result[0]
    else:
        raise ValueError("Response length is insufficient for the given number of registers.")

def extract_registers(function_code, start_addr, num_registers):
    response = send_modbus_request(function_code, start_addr, num_registers)
    return parse_modbus_response(response, num_registers)

def readInputRegisters(offset, num_registers=1):
    start_address = INPUT_REGISTER_BASE + offset
    return extract_registers(FUNCTION_CODE_INPUT, start_address, num_registers)

def readHoldingRegisters(offset, num_registers=1):
    start_address = HOLDING_REGISTER_BASE + offset
    return extract_registers(FUNCTION_CODE_HOLDING, start_address, num_registers)
