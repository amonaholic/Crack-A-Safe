from safe import Safe
import serial
import platform
import time


# Check which OS is in use
if platform.system() == "Windows":
    port = "COM3"
elif platform.system() == "Linux":
    port = "/dev/ttyUSB0"
else:
    raise RuntimeError("OS not supported")

# Open the serial connection to communicate with the ESP32
ser = serial.Serial(port, 115200)

# The ESP32 may restart when the serial connection is opened
time.sleep(2)

# Remove old startup messages from the serial input buffer
ser.reset_input_buffer()


try:
    # Create the Safe object and pass the serial connection to it
    safe = Safe(ser)

    # Generate a random passcode
    safe.passcode = safe.generate_passcode()

    # Debug output: show the generated passcode on the PC
    print("Passcode:", safe.passcode)

    # Start the safe cracking game
    safe.start_cracking()


finally:
    # Always close the serial connection when the program stops
    ser.close()