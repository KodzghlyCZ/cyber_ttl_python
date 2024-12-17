from .modbus import readHoldingRegisters, readInputRegisters
from .enums.ErrorCode import ErrorCode
from .maps.error import error_map
from .maps.sensor_gas_types import sensorGasTypeMap
from . import utils

# Function to calculate gas concentration
def calculate_concentration():
  try:
    return (
      (
        readInputRegisters(0x02)
        *
        (
          round(
            (
              readHoldingRegisters(0x00)
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
          readHoldingRegisters(0x07)
          >> 8
        )
      )
      /
      418
    )
  except Exception as e:
    print(f"Error: {e}")
    return None


def get_gas_name():
  try:
    return sensorGasTypeMap.get(
      (
        (
          utils.shift_low_byte(
            readHoldingRegisters(
              0x0E
            )
          )
        ) | (
          utils.get_high_byte(
            readHoldingRegisters(
              0x14
            )
          )
        )
      )
    )

  except Exception as e:
    print(f"Error: {e}")
    return GasType.UNKNOWN_GAS_TYPE


def get_error_state():
  try:
    return error_map.get(
      utils.get_high_byte(
        readHoldingRegisters(
          0x03
        )
      )
    )

  except Exception as e:
    print(f"Error: {e}")
    return ErrorCode.UNKNOWN_ERROR
