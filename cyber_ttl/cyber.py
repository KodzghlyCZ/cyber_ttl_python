from .modbus import ModbusDriver
from .enums.ErrorCode import ErrorCode
from .maps.error import error_map
from .maps.sensor_gas_types import sensorGasTypeMap
from . import utils

# Function to calculate gas concentration using the ModbusDriver instance
def calculate_concentration(modbus_driver):
    try:
        return (
            (
                modbus_driver.read_input_registers(0x02)
                *
                (
                    round(
                        (
                            modbus_driver.read_holding_registers(0x00)
                            *
                            418
                        )
                        /
                        4096
                    )
                )
                /
                10
                **
                (
                    utils.get_high_byte(
                        modbus_driver.read_holding_registers(0x07)
                    )
                )
            )
            /
            418
        )
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_gas_name(modbus_driver):
    try:
        return sensorGasTypeMap.get(
            (
                (
                    utils.shift_low_byte(
                        modbus_driver.read_holding_registers(0x0E)
                    )
                ) | (
                    utils.get_high_byte(
                        modbus_driver.read_holding_registers(0x14)
                    )
                )
            )
        )
    except Exception as e:
        print(f"Error: {e}")
        return GasType.UNKNOWN_GAS_TYPE


def get_error_state(modbus_driver):
    try:
        return error_map.get(
            utils.get_high_byte(
                modbus_driver.read_holding_registers(0x03)
            )
        )
    except Exception as e:
        print(f"Error: {e}")
        return ErrorCode.UNKNOWN_ERROR
