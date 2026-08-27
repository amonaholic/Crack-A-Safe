#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SH110X.h>

// MakeyLab OLED
// SH1107, 64x128 intern, danach gedreht
// I2C bewusst auf 100 kHz wegen unseres ESP32-Problems
Adafruit_SH1107 display(
  64,
  128,
  &Wire,
  -1,
  100000,
  100000
);

void setup() {
  Serial.begin(115200);

  // MakeyLab I2C
  Wire.begin(21, 22);
  Wire.setClock(100000);

  // OLED starten
  if (!display.begin(0x3C, true)) {
    while (1) {
      delay(1000);
    }
  }

  display.setRotation(1);
  display.setTextColor(SH110X_WHITE);
  display.setTextSize(1);

  display.clearDisplay();
  display.setCursor(0, 0);
  display.println("READY");
  display.display();

  // Optional auch an den PC melden
  Serial.println("READY");
}

void loop() {

  // Ist eine Nachricht vom PC angekommen?
  if (Serial.available()) {

    // Bis zum Zeilenumbruch lesen
    String text = Serial.readStringUntil('\n');

    // \r usw. entfernen
    text.trim();

    // Display löschen
    display.clearDisplay();

    // Cursor oben links
    display.setCursor(0, 0);

    // empfangenen Text anzeigen
    display.print(text);

    // Display aktualisieren
    display.display();
  }
}
