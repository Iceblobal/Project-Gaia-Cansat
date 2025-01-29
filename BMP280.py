import board
import busio
import adafruit_bmp280



def read_temperature(sensor):
    return sensor.temperature

def read_pressure(sensor):
    return sensor.pressure

print("BMP280 ready")




