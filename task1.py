name = input("Please enter your name: ")
name = name.strip()

def greet(name: str, greeting: str = "Hello") -> str:
    """we are returning a greeting message"""
    return f"{greeting}, {name}"

if name:
    print(greet(name))

else:
    print(greet("there"))