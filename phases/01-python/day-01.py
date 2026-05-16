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
