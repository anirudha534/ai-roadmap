from pathlib import Path

p = Path("numbers.txt")
#p.write_text("10\nabc\n25.5\n\n7\n-3\nhello")
p.write_text("abc\nhello")

lines = p.read_text().splitlines()

numbers = []

for line in lines:
    try:
        f = float(line)
        numbers.append(f)
    except ValueError:
        continue

if numbers:
    print(sum(numbers))
    print(min(numbers))
    print(max(numbers))

else:
    print("No valid numbers found")





