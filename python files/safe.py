import random
import time


class Safe:

    def __init__(self, ser):
        self.ser = ser
        self.passcode = None
        self.attempts = 0
        self.is_open = False


    # Generate a random passcode with 6 digits from 0 to 9
    def generate_passcode(self):

        self.passcode = []

        for _ in range(6):
            digit = random.randint(0, 9)
            self.passcode.append(digit)

        return self.passcode


    # Check whether the entered passcode is correct
    def check_passcode(self, entered_passcode):

        if entered_passcode == self.passcode:
            self.is_open = True
            return True

        else:
            return False


    # Wait for a confirmed digit from the rotary encoder
    def read_digit_from_encoder(self):

        while True:

            # Read one complete line from the Arduino
            line = self.ser.readline()

            # Convert received bytes into a normal string
            line = line.decode("utf-8").strip()

            # Debug output on the PC
            print("Arduino:", line)

            # The Arduino sends messages such as:
            # Confirmed: 6
            if line.startswith("Confirmed:"):

                value = line.split(":")[1].strip()

                return int(value)


    # Start the main safe-cracking game loop
    def start_cracking(self):

        guessed_passcode = []
        digit_index = 0

        # Continue until all digits of the passcode
        # have been entered correctly
        while digit_index < len(self.passcode):

            # Tell the Arduino that a new digit should be entered
            self.ser.write(b"Enter a digit\n")

            # Wait for input from the rotary encoder
            digit = self.read_digit_from_encoder()

            # Debug output on the PC
            print("Expected digit:", self.passcode[digit_index])
            print("Entered digit:", digit)


            # Entered digit is too small
            if digit < self.passcode[digit_index]:

                self.ser.write(b"Hint:\\nBigger number!\n")

                time.sleep(2.5)


            # Entered digit is too large
            elif digit > self.passcode[digit_index]:

                self.ser.write(b"Hint:\\nSmaller number!\n")

                time.sleep(2.5)


            # Entered digit is correct
            else:

                self.ser.write(b"Click! Correct digit.\n")

                time.sleep(2.5)

                guessed_passcode.append(digit)

                digit_index += 1


        # Check the complete passcode after all digits
        # have been entered correctly
        if self.check_passcode(guessed_passcode):

            self.ser.write(b"Click! The safe opened\n")

            time.sleep(1000)