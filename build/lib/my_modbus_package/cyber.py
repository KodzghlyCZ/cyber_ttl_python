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
