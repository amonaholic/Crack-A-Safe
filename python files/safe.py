import random
import time


class Safe:

    def __init__(self, ser):
        self.ser = ser
        self.passcode = None
        self.attempts = 0
        self.is_open = False


    # -----------------------------------------------------
    # TASK 1
    # Generate a random passcode.
    #
    # The passcode should:
    # - contain 6 digits
    # - only contain numbers from 0 to 9
    #
    # Example:
    # [4, 1, 8, 2, 2, 7]
    # -----------------------------------------------------
    def generate_passcode(self):

        self.passcode = []

        # TODO:
        # Generate six random digits
        # and add them to self.passcode.


        return self.passcode


    # -----------------------------------------------------
    # TASK 2
    # Check whether the entered passcode is correct.
    #
    # Return True if both passcodes are equal.
    # Otherwise return False.
    # -----------------------------------------------------
    def check_passcode(self, entered_passcode):

        # TODO:
        # Compare entered_passcode with self.passcode.


        return False


    # -----------------------------------------------------
    # Read a digit from the rotary encoder.
    #
    # This function is already implemented.
    # You do NOT have to change it.
    # -----------------------------------------------------
    def read_digit_from_encoder(self):

        while True:

            # Read one complete line from the Arduino
            line = self.ser.readline()

            # Convert bytes into text
            line = line.decode("utf-8").strip()

            # Debug output
            print("Arduino:", line)

            # The Arduino sends messages such as:
            # Confirmed: 6
            if line.startswith("Confirmed:"):

                value = line.split(":")[1].strip()

                return int(value)


    # -----------------------------------------------------
    # TASK 3
    # Implement the main game.
    # -----------------------------------------------------
    def start_cracking(self):

        guessed_passcode = []
        digit_index = 0


        # -------------------------------------------------
        # TASK 3.1
        #
        # Repeat the game until every digit of the
        # passcode has been guessed correctly.
        # -------------------------------------------------

        while digit_index < len(self.passcode):

            # Tell the Arduino that the player
            # should enter a digit.
            self.ser.write(b"Enter a digit\n")

            # Read the selected digit from the encoder.
            digit = self.read_digit_from_encoder()


            # Debug output
            print("Expected digit:", self.passcode[digit_index])
            print("Entered digit:", digit)


            # -------------------------------------------------
            # TASK 3.2
            #
            # Compare the entered digit with the current
            # digit of the passcode.
            #
            # Case 1:
            # The entered digit is too small.
            #
            # Case 2:
            # The entered digit is too large.
            #
            # Case 3:
            # The entered digit is correct.
            # -------------------------------------------------


            # TODO:
            # If the entered digit is too small:
            #
            # Send this message to the Arduino:
            #
            # self.ser.write(b"Hint:\\nBigger number!\n")
            #
            # Then wait for a short moment.



            # TODO:
            # If the entered digit is too large:
            #
            # Send this message:
            #
            # self.ser.write(b"Hint:\\nSmaller number!\n")
            #
            # Then wait for a short moment.



            # TODO:
            # If the digit is correct:
            #
            # 1. Send:
            #
            # self.ser.write(b"Click! Correct digit.\n")
            #
            # 2. Wait for a short moment
            #
            # 3. Add the digit to guessed_passcode
            #
            # 4. Increase digit_index by 1



        # -------------------------------------------------
        # TASK 4
        #
        # After all six digits have been entered,
        # check the complete passcode.
        # -------------------------------------------------

        # TODO:
        # Use check_passcode() to check guessed_passcode.
        #
        # If the passcode is correct, send:
        #
        # self.ser.write(b"Click! The safe opened\n")
