import time
from machine import Pin, RTC


ON = True
OFF = False
HIGH = 1
LOW = 0

#  Power to SHT1x, active Low, via MOSFET
en_SHT1x = Pin(6, Pin.OUT)
#  SCLK clock pin to SHT1x
SCLK = Pin(8, Pin.OUT)
# DATA pin to SHT1x
DATA = Pin(7, Pin.OPEN_DRAIN)
rtc = RTC()

def init_SHT1x_interface():
    # Initialise the pins
    en_SHT1x.value(1)
    SCLK.low()
    DATA.high()
    time.sleep(1)

def SHT1x_power(status):
    if status:
        # Power OFF SHT1x via MOSFET
        en_SHT1x.low()
    else:
        # Power ON SHT1x via MOSFET
        en_SHT1x.high()
    time.sleep_ms(20)
    

def SHT1x_soft_reset():
    """  """
    # 3 address bits, 5 command bits
    command = 0b000_11110
    send_command_ackn(command)
    time.sleep_ms(20)
 
    
def transmission_start():
    """Transmission Start Sequence for SHT1x"""
    SCLK.high()
    time.sleep_us(100)
    DATA.low()
    time.sleep_us(50)
    SCLK.low()
    time.sleep_us(100)
    SCLK.high()
    time.sleep_us(100)
    DATA.high()
    time.sleep_us(50)
    SCLK.high()
    time.sleep_us(100)


def send_command_ackn(command):
    """ Bit-bang the command, msb first; wait for acknowlegement"""    
    mask = 0b1000_0000
    for idx in range(8):
        SCLK.low()
        time.sleep_us(100)
        DATA.value((mask >> idx) & command)
        time.sleep_us(50)
        SCLK.high()
        time.sleep_us(100)
    # Release data line
    DATA.value(1)
    # Clock pulse for ACK
    for i in range(3):        
        SCLK.value(i & 0b1)
        time.sleep_us(100)
     

def measure_temperature():
    # 3 address bits, 5 command bits
    command = 0b0000_0011
    send_command_ackn(command)


def measure_humidity():
    # 3 address bits, 5 command bits
    command = 0b000_00101
    send_command_ackn(command)


def read_data():
    data = 0x0000
    for idx in range(16, 8, -1):
        SCLK.high()
        time.sleep_us(100)
        data <<= 1
        data |= DATA.value()
        SCLK.low()
        time.sleep_us(100)
        
    # Clock pulse for ACK
    for i in range(1, 3):        
        SCLK.value(i & 0b1)
        time.sleep_us(100)
        
    for idx in range(7, -1, -1):
        SCLK.high()
        time.sleep_us(100)
        data <<= 1
        data |= DATA.value()
        SCLK.low()
        time.sleep_us(100)
    # Clock pulse for ACK
    for i in range(1, 3):        
        SCLK.value(i & 0b1)
        time.sleep_us(100)
        
    return data

def read_crc():
    crc = 0b0
    for idx in range(8):
        SCLK.value(1)
        time.sleep_us(100)
        crc <<= 1
        crc |= DATA.value()
        SCLK.value(0)
        time.sleep_us(100)
    # Clock pulse for ACK
    for i in range(1, 3):        
        SCLK.value(i & 0b1)
        time.sleep_us(100)
        
    return crc


init_SHT1x_interface()

SHT1x_power(ON)
transmission_start()
SHT1x_soft_reset()

for n in range(240):

    transmission_start()
    measure_temperature()
    for i in range(200):
        time.sleep_ms(2)
        if DATA.value() == 0:            
            break

    T_readout = read_data()
    temperature = -39.67 + (0.01 * T_readout)
    time.sleep_ms(10)
    
    transmission_start()
    measure_humidity()
    for i in range(200):
        time.sleep_ms(2)
        if DATA.value() == 0:            
            break
        
    H_readout = read_data()
    humidity = -2.0468 + (0.0367 * H_readout) + (-1.5955e-6 * (H_readout**2))
    true_humidity = (temperature - 25) * (0.01 + (0.00008 * humidity)) + humidity

    print(f"{rtc.datetime()}; {temperature}; {humidity}")
    print(f"{rtc.datetime()}; {T_readout}; {H_readout}")
    SHT1x_power(OFF)
    time.sleep(30)

