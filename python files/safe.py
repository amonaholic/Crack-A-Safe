import random
import time
from http import server


class Safe:
    def __init__(self, ser):
        self.ser = ser
        self.passcode = None
        self.attempts = 0
        self.is_open = False

    def generate_passcode(self):
        self.passcode = []

        for _ in range(6):
            digit = random.randint(0,9)
            self.passcode.append(digit)

        return self.passcode

    def check_passcode(self, entered_passcode):
        if entered_passcode == self.passcode:
            self.is_open = True
            return True
        else:
            return False

    def start_cracking(self):
        guessed_passcode = []
        digit_index = 0

        while digit_index < len(self.passcode):
            self.ser.write(b"Enter a digit\n")

            digit = int(input())

            print("Gesuchte Ziffer:", self.passcode[digit_index])
            print("Eingabe:", digit)

            if digit < self.passcode[digit_index]:
                self.ser.write(b"Hint:\\nBigger number!\n")
                time.sleep(5)

            elif digit > self.passcode[digit_index]:
                self.ser.write(b"Hint:\\nSmaller number!\n")
                time.sleep(5)

            else:
                self.ser.write(b"Click! Correct digit.\n")
                time.sleep(5)
                guessed_passcode.append(digit)
                digit_index += 1

        if self.check_passcode(guessed_passcode):
            self.ser.write(b"Click! The safe opened")
            time.sleep(10)



