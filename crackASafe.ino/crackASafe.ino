#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SH110X.h>

// -------------------------
// Rotary encoder
// -------------------------
const int encoderA = 32;
const int encoderB = 35;
const int encoderButton = 15;

int previousA;
bool previousButton;
int encoderValue = 0;


// -------------------------
// MakeyLab OLED display
// -------------------------
// SH1107 display, internally 64x128 pixels.
// The display is rotated later.
//
// I2C is intentionally limited to 100 kHz
// because of compatibility issues with our ESP32 setup.
Adafruit_SH1107 display(
  64,
  128,
  &Wire,
  -1,
  100000,
  100000
);


// Show the currently selected digit on the OLED
void showEncoderValue() {
  display.clearDisplay();

  display.setCursor(0, 0);
  display.setTextSize(1);
  display.println("Enter a digit:");

  display.setTextSize(4);
  display.setCursor(50, 25);
  display.println(encoderValue);

  display.setTextSize(1);
  display.display();
}


// Show any text received from the PC on the OLED
void showText(String text) {
  display.clearDisplay();

  display.setCursor(0, 0);
  display.setTextSize(1);
  display.print(text);

  display.display();
}


void setup() {

  // Start serial communication with the PC
  Serial.begin(115200);


  // -------------------------
  // Initialize rotary encoder
  // -------------------------
  pinMode(encoderA, INPUT_PULLUP);
  pinMode(encoderB, INPUT);
  pinMode(encoderButton, INPUT_PULLUP);

  previousA = digitalRead(encoderA);
  previousButton = digitalRead(encoderButton);


  // -------------------------
  // Initialize MakeyLab I2C
  // -------------------------
  Wire.begin(21, 22);
  Wire.setClock(100000);


  // Start OLED display
  if (!display.begin(0x3C, true)) {

    // Stop here if the display could not be initialized
    while (1) {
      delay(1000);
    }
  }


  // Configure display
  display.setRotation(1);
  display.setTextColor(SH110X_WHITE);
  display.setTextSize(1);


  // Show startup message
  display.clearDisplay();
  display.setCursor(0, 0);
  display.println("READY");
  display.display();


  // Also notify the PC that the device is ready
  Serial.println("READY");
}


void loop() {

  // =====================================================
  // 1. Read rotary encoder
  // =====================================================

  int currentA = digitalRead(encoderA);


  // Detect a falling edge on encoder signal A
  if (currentA != previousA && currentA == LOW) {

    // Signal B determines the rotation direction
    if (digitalRead(encoderB) == HIGH) {

      // Count up:
      // 0 -> 1 -> 2 -> ... -> 9 -> 0
      if (encoderValue == 9) {
        encoderValue = 0;
      }
      else {
        encoderValue++;
      }

    }
    else {

      // Count down:
      // 0 -> 9 -> 8 -> ... -> 1 -> 0
      if (encoderValue == 0) {
        encoderValue = 9;
      }
      else {
        encoderValue--;
      }
    }


    // Send the current value to the PC for debugging
    Serial.print("Current value: ");
    Serial.println(encoderValue);


    // Show the current value on the OLED
    showEncoderValue();
  }


  // Remember the current state for the next loop iteration
  previousA = currentA;



  // =====================================================
  // 2. Read encoder button
  // =====================================================

  bool currentButton = digitalRead(encoderButton);


  // Detect a button press:
  // HIGH -> LOW means that the button was pressed
  if (currentButton == LOW && previousButton == HIGH) {

    // Send the confirmed digit to Python
    Serial.print("Confirmed: ");
    Serial.println(encoderValue);


    // Simple button debounce
    delay(30);
  }


  // Remember the current button state
  previousButton = currentButton;



  // =====================================================
  // 3. Receive messages from Python
  // =====================================================

  if (Serial.available()) {

    // Read until a newline character is received
    String text = Serial.readStringUntil('\n');


    // Remove unnecessary whitespace and carriage returns
    text.trim();


    // Convert the characters "\n" sent by Python
    // into an actual line break for the OLED
    text.replace("\\n", "\n");


    // If Python requests a new digit,
    // show the rotary encoder input screen
    if (text == "Enter a digit") {

      showEncoderValue();

    }
    else {

      // Display all other messages received from Python,
      // for example hints, correct digits or the open message
      showText(text);
    }
  }
}
