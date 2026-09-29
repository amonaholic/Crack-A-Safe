# Tutor Cheat Sheet – Crack-A-Safe

Dieser Spickzettel ist als kurze Hilfe für die Betreuung des Kurses gedacht.  
Er orientiert sich an den Aufgaben in `safe.py` und soll dir helfen, die nötigen Python-Konzepte in sinnvoller Reihenfolge zu erklären, ohne die Lösungen direkt vorzugeben.

---

## Ziel des Kurses

Die Teilnehmenden sollen die TODOs in `safe.py` selbstständig ergänzen können.

Dafür müssen sie vor allem verstehen:

- Listen
- Zufallszahlen
- `for`- und `while`-Schleifen
- `if / elif / else`
- Vergleiche
- Listen-Indizes
- `return`
- `self` und Methoden
- `append()`
- `len()`
- `time.sleep()`
- serielle Ausgabe mit `self.ser.write(...)`

Die serielle Eingabe vom Rotary Encoder ist bereits implementiert und muss nicht neu erklärt oder programmiert werden.

---

# Empfohlene Reihenfolge

## 1. Kurz erklären: Was ist `Safe`?

Zeige:

```python
class Safe:
```

Erklärung:

> Eine Klasse ist ein Bauplan für Objekte.

Im Hauptprogramm wird daraus ein Objekt erzeugt:

```python
safe = Safe(ser)
```

Dann können Methoden aufgerufen werden:

```python
safe.generate_passcode()
safe.start_cracking()
```

### `self`

Innerhalb der Klasse bedeutet:

```python
self
```

ungefähr:

> dieses konkrete Safe-Objekt

Beispiele:

```python
self.passcode
self.is_open
self.ser
```

Das sind Werte, die zum Safe gehören.

Nicht zu tief in OOP einsteigen. Für die Aufgabe reicht dieses Grundverständnis.

---

# TASK 1 – Passcode erzeugen

## Was müssen die Teilnehmenden verstehen?

### Leere Liste

```python
numbers = []
```

### Wert anhängen

```python
numbers.append(5)
```

### Schleife mit `range()`

```python
for _ in range(6):
    print("Hello")
```

Erklärung:

> Der Code innerhalb der Schleife wird sechsmal ausgeführt.

### Zufallszahl

```python
random.randint(0, 9)
```

Erklärung:

> Erzeugt eine zufällige ganze Zahl zwischen 0 und 9, inklusive 0 und 9.

---

## Leitfragen für TASK 1

Wenn jemand hängt, nicht sofort die Lösung geben.

Frage stattdessen:

- Wo sollen die erzeugten Zahlen gespeichert werden?
- Wie fügt man einer Liste einen Wert hinzu?
- Wie oft muss etwas wiederholt werden?
- Welche Funktion erzeugt eine Zufallszahl?
- Was sollte am Ende zurückgegeben werden?

---

## Typische Fehler

### `append()` vergessen

Falsch gedacht:

```python
digit = random.randint(0, 9)
```

Die Zahl wird erzeugt, aber nicht gespeichert.

### Falscher Bereich

Zum Beispiel:

```python
random.randint(0, 10)
```

Dann kann auch `10` entstehen.

### Nur eine Zahl erzeugt

Wenn keine Schleife verwendet wird, besteht der Passcode nicht aus sechs Stellen.

---

# TASK 2 – Passcode vergleichen

## Vergleiche erklären

```python
a == b
```

bedeutet:

> Sind `a` und `b` gleich?

Wichtig:

```python
a = 5
```

ist eine Zuweisung.

```python
a == 5
```

ist ein Vergleich.

---

## Listen können direkt verglichen werden

```python
list_a = [1, 2, 3]
list_b = [1, 2, 3]

list_a == list_b
```

ergibt:

```python
True
```

---

## `return`

Beispiel:

```python
def check(number):

    if number == 5:
        return True

    return False
```

Erklärung:

> `return` gibt einen Wert zurück und beendet die Funktion an dieser Stelle.

---

## Leitfragen für TASK 2

- Welche zwei Werte sollen miteinander verglichen werden?
- Kann Python zwei Listen direkt vergleichen?
- Was soll die Methode zurückgeben, wenn beide gleich sind?
- Was soll sie zurückgeben, wenn sie unterschiedlich sind?

---

# TASK 3 – Das eigentliche Spiel

Das ist der wichtigste Teil.

Die Teilnehmenden müssen verstehen, wie immer nur **eine Stelle des Passcodes** geprüft wird.

---

## Listen-Index erklären

```python
numbers = [4, 7, 2]

numbers[0]   # 4
numbers[1]   # 7
numbers[2]   # 2
```

Wichtig:

> Python beginnt bei Index 0.

Im Spiel:

```python
self.passcode[digit_index]
```

bedeutet:

> Die aktuell zu erratende Stelle des Passcodes.

---

# `while` erklären

Beispiel:

```python
index = 0

while index < 3:
    print(index)
    index += 1
```

Erklärung:

> Solange die Bedingung wahr ist, wird die Schleife wiederholt.

Im Projekt:

```python
while digit_index < len(self.passcode):
```

Bedeutung:

> Solange noch nicht alle Stellen des Passcodes richtig geraten wurden, läuft das Spiel weiter.

---

## `len()`

```python
len([4, 7, 2])
```

ergibt:

```python
3
```

---

# `if / elif / else`

Benutze zuerst ein neutrales Beispiel:

```python
number = 5

if number < 5:
    print("Too small")

elif number > 5:
    print("Too large")

else:
    print("Correct")
```

Dann auf das Spiel übertragen:

- Eingabe kleiner als gesuchte Zahl
- Eingabe größer als gesuchte Zahl
- sonst: Zahl ist korrekt

---

## Wichtigster Punkt in TASK 3

Der Index darf nur erhöht werden, wenn die Zahl korrekt geraten wurde.

Zeige das Prinzip:

```python
index += 1
```

Frage:

> Was würde passieren, wenn wir den Index auch bei einer falschen Zahl erhöhen?

Erwartete Erkenntnis:

> Das Spiel würde zur nächsten Stelle springen, obwohl die aktuelle Stelle noch nicht korrekt geraten wurde.

---

## `append()` im Spiel

Wenn eine Zahl korrekt ist, kann sie gesammelt werden:

```python
guessed_numbers.append(number)
```

Dadurch entsteht nach und nach eine vollständige Liste.

---

## Leitfragen für TASK 3

Wenn jemand nicht weiterkommt:

- Welche Zahl wurde eingegeben?
- Welche Zahl wird gerade gesucht?
- Wie greifst du auf die aktuelle Stelle des Passcodes zu?
- Welche drei Fälle gibt es?
- Was passiert bei „zu klein“?
- Was passiert bei „zu groß“?
- Was muss nur bei „korrekt“ passieren?
- Wann darf `digit_index` erhöht werden?
- Wo soll die richtige Zahl gespeichert werden?

---

# Serielle Ausgabe

Die Teilnehmenden müssen UART nicht im Detail verstehen.

Es reicht:

```python
self.ser.write(b"Hello\n")
```

Erklärung:

> Dieser Text wird an den ESP32 geschickt.

Das `b` bedeutet:

> Der Text wird als Bytes gesendet.

Das `\n` bedeutet:

> Zeilenumbruch.

Beispiel:

```python
self.ser.write(b"Hint:\nTry again!\n")
```

---

# `time.sleep()`

```python
time.sleep(2.5)
```

Erklärung:

> Das Python-Programm wartet 2,5 Sekunden.

Im Projekt wird das verwendet, damit Meldungen und Hinweise kurz sichtbar bleiben.

---

# TASK 4 – Spiel beenden

Nach der Schleife wurden alle sechs Stellen korrekt geraten.

Dann soll der vollständige Passcode noch einmal überprüft werden.

Die dafür vorgesehene Methode existiert bereits:

```python
self.check_passcode(...)
```

---

## `return` zum Beenden

Ein einfaches Beispiel:

```python
def game():

    print("Game finished")

    return
```

Erklärung:

> `return` beendet die Methode. Danach geht das Programm beim Aufrufer weiter.

Im Hauptprogramm läuft anschließend der `finally`-Block und die serielle Verbindung wird geschlossen.

---

## Leitfragen für TASK 4

- Welche Liste enthält alle korrekt geratenen Zahlen?
- Welche Methode kann prüfen, ob diese Liste korrekt ist?
- Welche Nachricht soll bei Erfolg an den ESP32 geschickt werden?
- Wie kann die Methode danach sauber beendet werden?

---

# Was du NICHT ausführlich erklären musst

Diese Teile sind bereits vorgegeben:

- `serial.Serial(...)`
- `readline()`
- `.decode(...)`
- `.strip()`
- `.split(...)`
- Betriebssystemerkennung
- COM-Ports / `/dev/ttyUSB0`
- interne Funktionsweise des Rotary Encoders
- UART-Protokoll im Detail

Falls jemand fragt, kannst du kurz erklären, was sie tun. Für das Lösen der TODOs sind sie aber nicht nötig.

---

# Gute Reihenfolge für eine Live-Erklärung

## Schritt 1 – Kleines Beispiel außerhalb des Projekts

```python
numbers = []

for _ in range(3):
    numbers.append(random.randint(0, 9))

print(numbers)
```

Hiermit kannst du erklären:

- Liste
- Schleife
- Zufallszahl
- `append()`

---

## Schritt 2 – Vergleich

```python
secret = 5
guess = 3

if guess < secret:
    print("Too small")

elif guess > secret:
    print("Too large")

else:
    print("Correct")
```

Hiermit erklärst du:

- Vergleich
- `if`
- `elif`
- `else`

---

## Schritt 3 – Index

```python
code = [4, 7, 2]
index = 0

print(code[index])
```

Dann:

```python
index += 1
print(code[index])
```

---

## Schritt 4 – Schleife

```python
code = [4, 7, 2]
index = 0

while index < len(code):

    print(code[index])

    index += 1
```

Jetzt haben sie fast alle Bausteine für TASK 3 gesehen.

---

# Typische Anfängerprobleme

## `=` statt `==`

```python
if number = 5:
```

ist falsch.

Richtig:

```python
if number == 5:
```

---

## Falsche Einrückung

Python verwendet Einrückungen als Teil der Syntax.

Beispiel:

```python
if number == 5:
    print("Correct")
```

---

## Klammern beim Methodenaufruf vergessen

Falsch:

```python
safe.generate_passcode
```

Richtig:

```python
safe.generate_passcode()
```

---

## `self.` vergessen

Innerhalb einer Klasse:

```python
self.passcode
```

nicht einfach:

```python
passcode
```

wenn das Attribut des Objekts gemeint ist.

---

## Endlosschleife

Bei:

```python
while index < 6:
```

muss sich `index` irgendwann verändern.

Sonst läuft die Schleife für immer.

---

## Index zu früh erhöhen

Besonders bei TASK 3 darauf achten:

> Der Index wird nur erhöht, wenn die aktuelle Stelle korrekt geraten wurde.

---

# Wenn jemand komplett festhängt

Gehe nicht direkt zur fertigen Codezeile.

Nutze diese Reihenfolge:

1. **Was soll passieren?**
2. **Welche Variable enthält die Information?**
3. **Welche Python-Struktur brauchen wir?**
   - Schleife?
   - Bedingung?
   - Liste?
4. **Wie sieht die Syntax dafür aus?**
5. **Lass die Person die konkrete Zeile selbst schreiben.**

---

# Kurzfassung für dich

## TASK 1

Erklären:

```text
Liste
append()
for
range()
random.randint()
```

## TASK 2

Erklären:

```text
==
if
return True / False
Listenvergleich
```

## TASK 3

Erklären:

```text
Index
list[index]
while
len()
if / elif / else
< und >
append()
index += 1
time.sleep()
self.ser.write()
```

## TASK 4

Erklären:

```text
Methodenaufruf
check_passcode(...)
return
```

---

# Merksatz

Die Studierenden müssen nicht lernen, wie das komplette System intern funktioniert.

Sie müssen verstehen, wie man mit wenigen Python-Bausteinen einen klaren Ablauf formuliert:

```text
Wert erzeugen
→ speichern
→ vergleichen
→ Entscheidung treffen
→ wiederholen
→ Spiel beenden
```
