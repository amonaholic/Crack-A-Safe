# Crack-A-Safe

A hands-on Python and IoT project in which players try to crack a randomly generated six-digit safe code.

The player selects digits from 0 to 9 using the rotary encoder on the MakeyLab and confirms each digit by pressing the encoder button. The currently selected digit, hints, and game status are displayed on the MakeyLab OLED.

Python handles the main game logic, including generating the random passcode, checking the entered digits, and deciding whether the next guess has to be higher or lower.

The ESP32 handles the hardware interaction, including reading the rotary encoder, displaying information on the OLED, and communicating with the Python application over a serial connection.

The goal of the project is to introduce students to basic Python programming concepts such as variables, lists, loops, conditions, functions, classes, and simple hardware communication.