from enum import Enum

class ErrorCode(Enum):
    NO_ERRORS = "No errors"
    HEATING = "Heating"
    E2PROM_ERROR = "E2PROM error"
    FLASH_ERROR = "Flash error"
    RAM_ERROR = "RAM error"
    VCC_ERROR = "VCC error"
    VGND_ERROR = "VGND error"
    E2PROM_CKSM_ERROR = "E2PROM CKSM error"
    CHANGE_SENSOR = "Change sensor"
    ANALOG_OUT_ERROR_4_20ma = "Analog out error 4-20mA"
    Heating_VGND_ERROR = "Heating VGND error"
    ADC_ERROR = "ADC error"
    UNKNOWN_ERROR = "Unknown error"  # Default for unknown errors