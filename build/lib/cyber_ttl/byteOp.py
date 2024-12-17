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
    
    return value & 0xFF  # Mask the lower 8 bits
