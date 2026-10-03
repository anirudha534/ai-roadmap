def greet(name: str, greeting: str = "Hello") -> str:
    """I am returning a greeting message"""
    return f"{greeting}, {name}"

print(greet("Anirudha"))
print(greet("Anirudha", "Namaste"))