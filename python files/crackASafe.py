from safe import Safe
import serial
import time

ser = serial.Serial("COM3", 115200)

time.sleep(2)

try:
    safe = Safe(ser)

    safe.passcode = safe.generate_passcode()
    safe.start_cracking()

    while True:
        time.sleep(1)

finally:
    ser.close()