import serial
import time

ser = serial.Serial("COM3", 115200)

try:
    ser.write(b"hello world!")
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    ser.write(b"program ending")
    time.sleep(5)
    ser.close()