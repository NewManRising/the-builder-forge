name = "Joe"
hourly_rate = 35.0
hours_worked = 40
tax_applied = False


if tax_applied:
    tax = 0.15
else:
    tax = 0.0

subtotal = hourly_rate * hours_worked
tax_amount = subtotal * tax

print("*** Invoice ***")
print(f"Freelancer: {name}")
print(f"Hours Worked: {hours_worked}")
print(f"Hourly_rate: ${hourly_rate:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Taxes (15%): ${tax_amount:.2f}")
print(f"Total Due: ${subtotal + tax_amount:.2f}")
