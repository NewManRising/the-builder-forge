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


def generate_invoice(name: str, hours: float, rate: float, tax_rate: float = 0.15) -> str:
    subtotal = hours * rate
    tax = calculate_tax(subtotal, tax_rate)
    total = subtotal + tax
    return f"*** Invoice ***\nName: {name}\nHours: {hours}\nRate: ${rate:.2f}/hr\nSubtotal: ${subtotal:.2f}\nTax: ${tax:.2f}\nTotal: ${total:.2f}"


print(generate_invoice("Matthew", 45.8, 25.0))
