import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import os
import sys

resistor_ratio = 3.136


# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)

print("{:>5}\t{:>5}".format('raw', 'v'))

while True:
#    print("{:>5.3}\t{:>5.3f}".format(chan.voltage, chan.voltage*resistor_ratio))
#    time.sleep(0.5)
    
    if ((chan.voltage)*resistor_ratio) < 13:
        os.system('python Battery1On_Battery2Off.py')