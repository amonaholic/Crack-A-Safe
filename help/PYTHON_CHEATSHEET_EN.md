# Python Cheat Sheet – Crack-A-Safe

This cheat sheet contains the most important Python basics you need for the tasks in `safe.py`.

> **Goal:** Use these examples as a syntax reference. The examples do not directly solve the tasks for you.

---

## 1. Variables

A variable stores a value:

```python
number = 5
name = "Alice"
is_ready = False
```

You can use the value later:

```python
print(number)
```

---

## 2. Lists

A list can store multiple values:

```python
numbers = [4, 1, 8, 2]
```

An empty list:

```python
numbers = []
```

### Add a value: `append()`

```python
numbers.append(7)
```

The list now contains:

```python
[7]
```

Adding multiple values:

```python
numbers = []

numbers.append(3)
numbers.append(8)
numbers.append(1)
```

Result:

```python
[3, 8, 1]
```

---

## 3. Accessing List Elements

Python starts counting list positions at **0**:

```python
numbers = [4, 7, 2]

print(numbers[0])   # 4
print(numbers[1])   # 7
print(numbers[2])   # 2
```

A variable can also be used as an index:

```python
index = 1
print(numbers[index])   # 7
```

---

## 4. List Length: `len()`

Use `len()` to get the number of elements in a list:

```python
numbers = [4, 7, 2]

print(len(numbers))   # 3
```

Example:

```python
index = 0

if index < len(numbers):
    print("There is still an element left.")
```

---

## 5. `for` Loops

A `for` loop repeats code:

```python
for i in range(3):
    print(i)
```

Output:

```text
0
1
2
```

If you do not need the loop counter, you can use `_`:

```python
for _ in range(6):
    print("Hello")
```

This code runs six times.

---

## 6. Random Numbers

The project imports the `random` module.

You can generate a random integer between 0 and 9 like this:

```python
digit = random.randint(0, 9)
```

Example:

```python
for _ in range(3):
    digit = random.randint(0, 9)
    print(digit)
```

---

## 7. Comparisons

Python can compare values:

```python
a = 3
b = 7
```

| Expression | Meaning |
|---|---|
| `a == b` | equal |
| `a != b` | not equal |
| `a < b` | less than |
| `a > b` | greater than |
| `a <= b` | less than or equal |
| `a >= b` | greater than or equal |

Important:

```python
a = 5
```

assigns a value.

```python
a == 5
```

checks whether `a` is equal to `5`.

---

## 8. `if`, `elif`, `else`

Conditions decide which code should run:

```python
number = 5

if number < 5:
    print("Too small")

elif number > 5:
    print("Too large")

else:
    print("Exactly right")
```

`else` runs if none of the previous conditions are true.

---

## 9. Comparing Lists

Two lists can be compared directly:

```python
list_a = [1, 2, 3]
list_b = [1, 2, 3]

if list_a == list_b:
    print("The lists are equal.")
```

The order of the elements must also match.

---

## 10. `while` Loops

A `while` loop runs as long as its condition is `True`:

```python
index = 0

while index < 3:
    print(index)
    index += 1
```

Output:

```text
0
1
2
```

Make sure the condition can eventually become false. Otherwise, you create an infinite loop.

---

## 11. Increasing Numbers: `+=`

Instead of writing:

```python
index = index + 1
```

you can write:

```python
index += 1
```

Both do the same thing.

---

## 12. Functions and Methods

A normal function looks like this:

```python
def greet(name):
    print("Hello", name)
```

Call it like this:

```python
greet("Sam")
```

A function can return a value:

```python
def double(number):
    return number * 2
```

Call:

```python
result = double(4)
print(result)   # 8
```

---

## 13. `return`

`return` has two important uses.

### Return a value

```python
def is_even(number):

    if number % 2 == 0:
        return True

    return False
```

### End a function or method

```python
def finish():

    print("Finished!")

    return
```

After `return`, no more code in that function is executed.

---

## 14. Classes, Objects, and `self`

The project contains the class:

```python
class Safe:
```

An object of this class can be created like this:

```python
safe = Safe(ser)
```

### `self`

Inside a class, `self` means:

> this specific object

Example:

```python
class Player:

    def __init__(self):
        self.score = 0
```

Each `Player` object gets its own `score`.

---

## 15. Attributes

An attribute is a variable that belongs to an object:

```python
self.passcode = []
self.attempts = 0
self.is_open = False
```

Inside the class, access it with `self`:

```python
print(self.passcode)
```

Outside the class, access it through the object:

```python
print(safe.passcode)
```

---

## 16. Calling Methods

A method belongs to a class.

Example:

```python
class Player:

    def say_hello(self):
        print("Hello!")
```

Call it like this:

```python
player = Player()
player.say_hello()
```

Methods can also call other methods of the same class:

```python
self.say_hello()
```

---

## 17. Waiting: `time.sleep()`

With:

```python
time.sleep(2)
```

the program waits for two seconds.

Example:

```python
print("Start")
time.sleep(1)
print("Continue")
```

In this project, this is useful for keeping hints visible for a short time.

---

## 18. Sending Messages to the ESP32

The project uses the serial connection through `self.ser`.

Send a message like this:

```python
self.ser.write(b"Hello\n")
```

The `b` before the string means that the text is sent as **bytes**.

Example:

```python
self.ser.write(b"Try again\n")
```

`\n` means a line break.

### Multiple lines

```python
self.ser.write(b"Hint:\nTry again!\n")
```

This is displayed approximately as:

```text
Hint:
Try again!
```

---

## 19. Boolean Values

Python has two boolean values:

```python
True
False
```

Example:

```python
door_open = False

if code_correct:
    door_open = True
```

---

## 20. Comments

Comments start with `#`:

```python
# This is a comment
number = 5
```

Python ignores comments when running the program.

---

## 21. Indentation Matters

Python uses indentation to determine which code belongs together:

```python
if number > 5:
    print("greater")
    print("This code belongs to the if block")

print("This code is outside the if block")
```

Usually, Python code uses **4 spaces** per indentation level.

---

## 22. Common Pattern: Comparing an Element

This general pattern is useful for many tasks:

```python
values = [2, 5, 8]
index = 0
entered_value = 4

if entered_value < values[index]:
    print("Too small")

elif entered_value > values[index]:
    print("Too large")

else:
    print("Correct")
```

Think about **when** the `index` should be increased.

---

## 23. Common Pattern: Collecting Values

You can collect correct inputs in a list:

```python
results = []

value = 4
results.append(value)
```

After several rounds, the list might look like this:

```python
[4, 1, 8]
```

---

## 24. Common Pattern: Looping Through Multiple Positions

```python
values = [3, 6, 9]
index = 0

while index < len(values):

    print(values[index])

    index += 1
```

This lets you process each position in a list one after another.

---

## 25. Debug Output

Use `print()` to check what your program is doing:

```python
print("index:", index)
print("value:", value)
print("list:", values)
```

If something does not work, debug output often helps you find where the problem is.

---

# What You Especially Need for `safe.py`

For the tasks in `safe.py`, you should be comfortable with:

```text
[]
append()
for ... in range(...)
random.randint(...)
if / elif / else
==  <  >
return
while
len(...)
list[index]
index += 1
time.sleep(...)
self.ser.write(...)
```

You do not need to reimplement the existing method that reads values from the rotary encoder.

---

## Quick Checklist When Something Does Not Work

Check the following:

- Is the indentation correct?
- Did I confuse `=` and `==`?
- Am I accessing the correct list position?
- Do I increase the index only when it makes sense?
- Can my `while` loop eventually end?
- Did I use `self.` when accessing methods or attributes inside the class?
- Did I forget `()` when calling a function or method?
- Did I save the file before running the program?

---

Good luck cracking the safe! 🔐
