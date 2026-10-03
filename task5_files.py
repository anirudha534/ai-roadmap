from pathlib import Path

p = Path("notes.txt")
p.write_text("Welcome \n to the \n Jungle")
text = p.read_text()
print(text)

print(text.splitlines())
lines = [line.strip() for line in text.splitlines()]

print(lines)

missing = Path("does_not_exist.txt")

try:
    print(missing.read_text())
except FileNotFoundError:
    print("That file does not exist")