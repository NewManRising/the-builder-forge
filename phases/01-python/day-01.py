age = 33
height = 5.11
name = "Matthew"
employed = False

print(type(age), type(height), type(name), type(employed))
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Name: {name}")
print(f"Employed: {employed}")


age_as_string = "33"
print(type(age_as_string))

age_converted = int(age_as_string)
print(type(age_converted))

print(age_converted + 10)

bio = "  my name is matthew and i build things with python.  "
strip = bio.strip()
capitalize = bio.strip().capitalize()
upper = bio.upper()
replace = bio.replace("python", "Python")
count = bio.count("i")
contains_word = "build" in bio

print(f"Original String: {bio}")
print(f"Stripped String: {strip}")
print(f"Capitalized String: {capitalize}")
print(f"Uppercase String: {upper}")
print(f"Replaced String: {replace}")
print(f"Count of 'i': {count}")
print(f"Contains 'build': {contains_word}")


a = 17
b = 5
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplkication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulo: {a} % {b} = {a % b}")
print(f"Power: {a} ** {b} = {a ** b}")


print(type(a / b))
print(type(a // b))
