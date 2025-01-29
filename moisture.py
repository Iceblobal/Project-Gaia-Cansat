import board
from analogio import AnalogIn

def read_moisture():
    return AnalogIn(board.GP26)

print("moisture ready")
