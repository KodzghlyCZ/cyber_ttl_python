import serial
import serial.rs485
import struct

class ModbusDriver:
    FUNCTION_CODE_HOLDING = 0x03
    FUNCTION_CODE_INPUT = 0x04
    SLAVE_ID = 0x00
    INPUT_REGISTER_BASE = 0x1000
    HOLDING_REGISTER_BASE = 0x2000

    def __init__(self, device, rs485=False, baudrate=9600, timeout=1):
        self.device = device
        self.rs485 = rs485
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None

    def open_serial_connection(self):
        """Opens the serial connection with RS232 or RS485 settings."""
        if self.serial_connection is None:
            if self.rs485:
                self.serial_connection = serial.rs485.RS485(
                    port=self.device, baudrate=self.baudrate, timeout=self.timeout
                )
                self.serial_connection.rs485_mode = serial.rs485.RS485Settings(
                    rts_level_for_tx=True,
                    rts_level_for_rx=False,
                    delay_before_tx=0.01,
                    delay_before_rx=0.01
                )
            else:
                self.serial_connection = serial.Serial(
                    self.device, baudrate=self.baudrate, timeout=self.timeout
                )
            print(f"Serial connection opened on {self.device} (RS485={self.rs485})")
        else:
            print("Serial connection is already open")

    def close_serial_connection(self):
        """Closes the serial connection."""
        if self.serial_connection is not None:
            self.serial_connection.close()
            self.serial_connection = None
            print("Serial connection closed")
        else:
            print("Serial connection is already closed")

    def calculate_crc16(self, data):
        """Calculates CRC16 checksum for Modbus RTU."""
        crc = 0xFFFF
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if crc & 0x0001:
                    crc = (crc >> 1) ^ 0xA001
                else:
                    crc >>= 1
        return struct.pack('<H', crc)

    def create_modbus_request(self, function_code, start_addr, num_registers):
        """Creates a Modbus RTU request frame."""
        request_frame = struct.pack('>B', self.SLAVE_ID)
        request_frame += struct.pack('>B', function_code)
        request_frame += struct.pack('>H', start_addr)
        request_frame += struct.pack('>H', num_registers)
        request_frame += self.calculate_crc16(request_frame)
        return request_frame

    def send_modbus_request(self, function_code, start_addr, num_registers):
        """Sends a Modbus request and receives the response."""
        if self.serial_connection is None:
            raise Exception("Serial connection is not open")

        request_frame = self.create_modbus_request(function_code, start_addr, num_registers)
        print(f"Request Frame (hex): {request_frame.hex()}")

        self.serial_connection.write(request_frame)
        response = self.serial_connection.read(5 + num_registers * 2)
        print(f"Response Frame (hex): {response.hex()}")
        return response

    def parse_modbus_response(self, response, num_registers, force_array=False):
        """Parses the Modbus response and extracts register values."""
        if len(response) >= 5 + num_registers * 2:
            data = response[3:-2]
            result = [
                struct.unpack('>H', data[i:i+2])[0]
                for i in range(0, len(data), 2)
            ]
            return result if force_array or len(result) > 1 else result[0]
        else:
            raise ValueError("Response length is insufficient for the given number of registers.")

    def extract_registers(self, function_code, start_addr, num_registers):
        """Extracts registers from a Modbus response."""
        response = self.send_modbus_request(function_code, start_addr, num_registers)
        return self.parse_modbus_response(response, num_registers)

    def read_input_registers(self, offset, num_registers=1):
        """Reads input registers using Modbus function 0x04."""
        start_address = self.INPUT_REGISTER_BASE + offset
        return self.extract_registers(self.FUNCTION_CODE_INPUT, start_address, num_registers)

    def read_holding_registers(self, offset, num_registers=1):
        """Reads holding registers using Modbus function 0x03."""
        start_address = self.HOLDING_REGISTER_BASE + offset
        return self.extract_registers(self.FUNCTION_CODE_HOLDING, start_address, num_registers)

