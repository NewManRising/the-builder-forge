def calculate_tip(bill: float, tip_percent: float = 0.18) -> float:
    tip = bill * tip_percent
    return tip


def split_bill(amount: float, people: int) -> float:
    return amount / people


def dinner_summary(bill: float, tip_percent: float = 0.18, people: int = 2) -> str:
    tip = calculate_tip(bill, tip_percent)
    total = bill + tip
    per_person = split_bill(total, people)
    return f"*** Dinner Summary ***\nBill: ${bill:.2f}\nTip: ${tip:.2f}\nTotal: ${total:.2f}\nPeople: {people}\nPer Person: ${per_person:.2f}"


print(dinner_summary(88.77, 0.2, 4))
