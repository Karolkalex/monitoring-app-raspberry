import time
import board
import busio
from adafruit_max30102 import MAX30102
from Adafruit_MCP3008 import MCP3008

# Setup I2C for MAX30100 (Pulse Oximeter)
i2c = busio.I2C(board.SCL, board.SDA)
pox = MAX30102(i2c)

# Setup SPI for MCP3008 (Heart Rate Sensor)
CLK = 11  # GPIO 11, SCLK
MISO = 9  # GPIO 9, MISO
MOSI = 10  # GPIO 10, MOSI
CS = 8  # GPIO 8, CE0
mcp = MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

class Sensor:
    def __init__(self):
        pass

    def get_heart_rate(self):
        # Read from MCP3008 channel 0 (Pulse Sensor)
        heart_rate_raw = mcp.read_adc(0)
        heart_rate = self.map_value(heart_rate_raw, 0, 1023, 40, 180)
        return heart_rate

    def get_spo2(self):
        # Read SpO2 and Heart Rate from MAX30100
        pox_values = pox.get_data()
        heart_rate = pox_values.heart_rate
        spo2 = pox_values.oxygen
        return heart_rate, spo2

    @staticmethod
    def map_value(value, in_min, in_max, out_min, out_max):
        # Function to map values from one range to another
        return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def disconnect(self):
        pass
