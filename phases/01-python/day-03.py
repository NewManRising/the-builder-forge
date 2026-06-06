def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to The Builder Forge!"


def calculate_tax(amount: float, rate: float = 0.15) -> float:

    tax = amount * rate
    return tax


def is_even(number: int) -> bool:
    return number % 2 == 0


print(greet("Matthew"))
print(calculate_tax(1400))
print(calculate_tax(1400, 0.08))
print(is_even(7))
print(is_even(12))
