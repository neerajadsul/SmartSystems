import time
import board
from adafruit_shtc3 import SHTC3
from adafruit_ltr329_ltr303 import LTR303
import busio
import bitbangio
from digitalio import Pull, DigitalInOut
import wifi
import os
import socketpool
import adafruit_requests
import rtc

real_time_clock = rtc.RTC()

class THLData():
    def __init__(self, location, timesecs, T, RH, LUX):
        self.location = location
        self.timesecs = timesecs
        self.T = T
        self.RH = RH
        self.LUX = LUX

    def __str__(self):
        return "{" + f'''"location":'{self.location}',"timesecs":{self.timesecs},"T":{self.T},"RH":{self.RH},"LUX":{self.LUX}''' + "}"

def get_als_reading(ltr):
    while True:
        ltr303.throw_out_reading()
        if ltr.new_als_data_available:
            ltr303.throw_out_reading()
            if ltr303.als_data_invalid:
                ltr303.throw_out_reading()
                continue
        for i in range(2):
            lux_visible = ltr303.visible_plus_ir_light
            lux_ir = ltr303.ir_light
        # print("VisibleIR: %.1f, IR: %.1f" % (lux_visible, lux_ir))
        break
    return (lux_visible, lux_ir)

def get_sht_reading(sht):
    T, RH = sht.measurements
    return T, RH

homewatcher_server = "http://192.168.1.19:8080/thlmonitor/sensor_data"


print("Connecting to Wi-Fi")
status = wifi.radio.connect(
    os.getenv("CIRCUITPY_WIFI_SSID"),
    os.getenv("CIRCUITPY_WIFI_PASSWORD")
    )

pool = socketpool.SocketPool(wifi.radio)
print("IP Address:", wifi.radio.ipv4_address)

requests = adafruit_requests.Session(pool)

i2c = busio.I2C(
        board.GP5, board.GP4
    )

# SHTC3 Temperature Humidity Sensor
sht = SHTC3(i2c)

# LTR-303ALS-01 Sensor
ltr303 = LTR303(i2c)
ltr303.als_gain = 96
ltr303.integration_time = 100
ltr303.measurement_rate = 200
als_data = get_als_reading(ltr303)
time.sleep(0.2)

# GET request obtains timesecs, current time as integer
response = requests.get(homewatcher_server)
print(response.text)
real_time_clock.datetime = time.localtime(int(response.text))

def send_data():
    T, RH = get_sht_reading(sht)
    print("T: %0.1fC, H: %0.1f %%" % (T, RH))

    als_data = get_als_reading(ltr303)
    print("LTR: ", als_data)

    thl_data = THLData(
            os.getenv("LOCATION"),
            time.time(),
            T,
            RH,
            als_data
        )
    print(str(thl_data))
    response = requests.post(homewatcher_server, data=str(thl_data))
    print(response.text)


packet_count = 0
while True:
    send_data()
    packet_count += 1
    if packet_count > 5:
        break
    time.sleep(3)
