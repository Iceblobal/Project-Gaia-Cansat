import adafruit_ltr390
import adafruit_bmp280
import radio
import bmp280
import uv
import moisture
import time
import digitalio
import board
import busio

i2c = busio.I2C(scl = board.GP15, sda = board.GP14)
bmp280_sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x77)
ltr390_sensor = adafruit_ltr390.LTR390(i2c)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True
packet_count = 0

time_from_launch = 0

wetness = moisture.read_moisture()

while True:
    temperature = bmp280.read_temperature(bmp280_sensor)
    pressure = bmp280.read_pressure(bmp280_sensor)
    uv_radiation = uv.read_uv(ltr390_sensor)

    print("############################ TIME FROM LAUNCH: " + str(time_from_launch) + " seconds")
    print("UV radiation: " + str(uv_radiation))
    print("Temperature: " + str(temperature))
    print("Pressure: " + str(pressure))
    print("Moisture: " + str(wetness.value))

    time_from_launch += 2

    led.value = not led.value
    print("tx")
    radio.send("UV: " + str(uv_radiation))
    radio.send("temperature: " + str(temperature))
    radio.send("pressure: " + str(pressure) + " uv: " + str(uv_radiation) + " temperature: " + str(temperature))
    radio.send("pressure: " + str(pressure) + " uv: " + str(uv_radiation) + " temperature: " + str(temperature))
    print("tx sent")
    time.sleep(2)


