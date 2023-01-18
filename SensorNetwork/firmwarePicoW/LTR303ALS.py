"""SHTC3 Temperature Humidity Sensor Driver"""

from machine import Pin, I2C
import time
from struct import unpack


class ALS():
    """Handles communication with SHTC3 Sensor"""
    
    I2C_ADDRESS = 0x29
    CONTROL = 0x80
    MEAS_RATE = 0x85
    DATA_CH1 = (0x88, 0x89)
    DATA_CH0 = (0x8A, 0x8B)
    STATUS = 0x8C 
    
    def __init__(self, i2c, scl, sda, freq=100_000):
        """initialization of I2C port"""
        
        assert type(scl) == Pin
        assert type(sda) == Pin
        self.i2c = I2C(i2c, scl=scl, sda=sda, freq=freq)
        devices = self.i2c.scan()    
        assert devices[0] == self.I2C_ADDRESS
        self.measurement_triggered = False
        
    def get_sensor_status(self):
        data = self.i2c.readfrom_mem(self.I2C_ADDRESS, self.STATUS, 1)
        data = int.from_bytes(data, "little")
        new_data_status = data and 0x04
        data_valid_status = data & 0x80
        gain_status = (data & 0b01110000) >> 4
        return new_data_status, data_valid_status, gain_status
    
    def sensor_sleep(self):
        self.i2c.writeto_mem(
                self.I2C_ADDRESS,
                self.CONTROL,
                str(0x00)
            )

    def sensor_wakeup(self, gain=1):        
        self.i2c.writeto_mem(
                self.I2C_ADDRESS,
                self.CONTROL,
                str(0x01)
            )
        
    def start_measurement(self, int_time, rate):
        self.i2c.writeto_mem(
                self.I2C_ADDRESS,
                self.M
            )
        
    def read_data(self):
        ch0 = self._read_channel(self.DATA_CH0)
        ch1 = self._read_channel(self.DATA_CH1)
        
        return ch0, ch1
    
    def _read_channel(self, addr):        
        LOWER = 0
        UPPER = 1
        total = 0
        data = self.i2c.readfrom_mem(self.I2C_ADDRESS, addr[LOWER], 1)
        data = int.from_bytes(data, "little")
        total += data
        data = self.i2c.readfrom_mem(self.I2C_ADDRESS, addr[UPPER], 1)
        data = int.from_bytes(data, "little")
        total += (data << 8)
        return total
    
    def get_temperature(self):
        T = None
        return T
    
    def get_humidity(self):
        RH = None
        return RH
        
sensor = ALS(1, scl = Pin(3), sda = Pin(2), freq=100_000)
sensor.sensor_sleep()
time.sleep(0.02)
sensor.sensor_wakeup()
time.sleep(0.02)
num_attemps = 0
while num_attemps < 10:
    print(sensor.get_sensor_status())
    time.sleep(0.5)
    print(sensor.read_data())
    time.sleep(1.5)
    num_attemps += 1
