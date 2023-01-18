"""SHTC3 Temperature Humidity Sensor Driver"""

from machine import Pin, SoftI2C
import time


class SHTC3():
    """Handles communication with SHTC3 Sensor"""
    
    I2C_ADDRESS = 0x70
    ID_REGISTER = bytearray(0xEF, 0xC8)
    CMD_SLEEP = bytearray(0xB0, 0x98)
    CMD_WAKEUP = bytearray(0x35, 0x17)
    CMD_SOFTRESET = bytearray(0x80, 0x5D)
    CMD_READ_T_FIRST = bytearray(0x78, 0x66)
    CMD_READ_RH_FIRST = bytearray(0x58, 0xE0)
    
    def __init__(self, i2c, scl, sda, freq=400_000):
        """initialization of I2C port"""        
        assert type(scl) == Pin
        assert type(sda) == Pin
        self.i2c = SoftI2C(scl=scl, sda=sda, freq=freq)
        devices = self.i2c.scan()
        if len(devices) == 0:
            raise Exception("Sensor Not Found")
        assert devices[0] == self.I2C_ADDRESS
        
    def get_sensor_id(self):
        if self.i2c.writeto(self.I2C_ADDRESS, self.ID_REGISTER, False):
            print("ID Command OK")
        time.sleep(0.01)
        self.sensor_id = self.i2c.readfrom(self.I2C_ADDRESS, 3, False)         
        return self.sensor_id
        
    def sensor_sleep(self):
        if self.i2c.writeto(self.I2C_ADDRESS, str(self.CMD_SLEEP)):
            print("Sleep OK")

    def sensor_wakeup(self):
        if self.i2c.writeto(self.I2C_ADDRESS, str(self.CMD_WAKEUP)):
            print("Wakeup OK")
        
    def start_measurement(self, RH_first = False):
        if RH_first:
            self.i2c.writeto(self.I2C_ADDRESS, str(self.CMD_READ_RH_FIRST))
        else:
            self.i2c.writeto(self.I2C_ADDRESS, str(self.CMD_READ_T_FIRST))
        
    def read_data(self):    
        data = self.i2c.readfrom(self.I2C_ADDRESS, 6)
        return data
    
    def get_temperature(self):
        T = None
        return T
    
    def get_humidity(self):
        RH = None
        return RH
        
try:        
    sensor = SHTC3(0, scl = Pin(5), sda = Pin(4), freq=10_000)
    sensor.sensor_sleep()
    time.sleep(0.02)
    sensor.sensor_wakeup()
    time.sleep(0.02)
    print(sensor.get_sensor_id())
    
except Exception as e:
    print("Error: ", e)

    
# sensor.start_measurement()
# time.sleep(0.05)
# data = sensor.read_data()
# T = sensor.get_temperature()
# RH = sensor.get_humidity()
# print(T, RH)
        