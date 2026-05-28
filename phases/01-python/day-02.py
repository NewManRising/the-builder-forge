

score = int(input("Enter A Score between 0 and 100: "))
print(f"Score: {score}")

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


skills = ["Python", "FastAPI", "SQL", "React", "Docker"]

for i, v in enumerate(skills, 1):
    print(f"{i}. {v}")


for n in range(1, 21):
    if n % 2 == 0:
        print(f"{n} is even")


secret = 7

while True:
    guess = int(input('Guess a Number Between 1 and 10: '))
    if guess == secret:
        print("Correct! You got it.")
        break
    elif guess < secret:
        print("Too low! Please Try Again.")
    else:
        print("Too high! Please Try Again.")


for n in range(1, 11):
    if n % 3 == 0:
        continue
    print(n)
