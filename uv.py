import adafruit_ltr390
import board
import busio

def read_uv(sensor):
    return sensor.uvs


print("ltr390 ready")
