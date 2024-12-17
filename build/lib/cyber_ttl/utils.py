def get_high_byte(value):
    """
    Extract the high byte from a 16-bit value.

    Args:
        value (int): A 16-bit integer value (0-65535).

    Returns:
        int: The high byte (8-bit value).
    """
    if not 0 <= value <= 0xFFFF:
        raise ValueError("Value must be a 16-bit integer (0-65535).")
    
    return (value >> 8) & 0xFF  # Shift right 8 bits and mask lower 8 bits


def get_low_byte(value):
    """
    Extract the low byte from a 16-bit value.

    Args:
        value (int): A 16-bit integer value (0-65535).

    Returns:
        int: The low byte (8-bit value).
    """
    if not 0 <= value <= 0xFFFF:
        raise ValueError("Value must be a 16-bit integer (0-65535).")
    
    return value & 0x00FF  # Mask the lower 8 bits

def mask_high_byte(value):
    """
    Mask the high byte of a 16-bit value (zeroes out the lower 8 bits).

    Args:
        value (int): A 16-bit integer value (0-65535).

    Returns:
        int: The masked value with only the high byte preserved (upper 8 bits).
    """
    if not 0 <= value <= 0xFFFF:
        raise ValueError("Value must be a 16-bit integer (0-65535).")

    return value & 0xFF00  # Mask the lower 8 bits to preserve only the high byte

def shift_low_byte(value):
    """
    Shift the low byte of a 16-bit value into the high byte position.

    Args:
        value (int): A 16-bit integer value (0-65535).

    Returns:
        int: The value with the low byte shifted to the high byte position.
    """
    if not 0 <= value <= 0xFFFF:
        raise ValueError("Value must be a 16-bit integer (0-65535).")
    
    return (value & 0x00FF) << 8  # Isolate the low byte and shift it 8 bits to the left
