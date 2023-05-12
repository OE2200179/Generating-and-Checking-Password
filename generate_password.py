import random

capital_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_alphabets = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
special_char = "!@#$%^&*()-+"

DICTIONARY = [
    "password",
    "cyber",
    "security",
    "hack",
    "omar",
    "morcy",
    "2000",
    "conventry",
    "pasta",
    "dog"
]

NAMES = [
    "omar",
    "morcy",
    "william",
    "john",
    "doe",
    "jane",
    "joe",
    "james",
    "jim",
    "jimmy",
]

# generate common phrases


def generate_common_phrases():
    phrases = []
    for i in range(100):
        phrases.append("".join(random.choice(small_alphabets + capital_alphabets + digits + special_char)
                               for _ in range(random.randint(2, 5))))
    return phrases


COMMON_PHRASES_GENERATED = generate_common_phrases()


def password_checker(password):
    s = password
    lower, upper, Sp, di = 0, 0, 0, 0
    if (len(s) >= 8):
        for i in s:
            # counting lowercase alphabets
            if (i in small_alphabets):
                lower += 1

            # counting uppercase alphabets
            if (i in capital_alphabets):
                upper += 1

            # counting digits
            if (i in digits):
                di += 1

            # counting the mentioned special characters
            if (i in special_char):
                Sp += 1

    if (lower >= 1 and upper >= 1 and Sp >= 1 and di >= 1):
        print("Strong Password")
    elif (Sp == 0 and lower >= 1 and upper >= 1 and di >= 1):
        print("Moderate Password")
    else:
        print("Weak Password")


def generate_password():
    password = ""
    for i in range(2):
        password += random.choice(small_alphabets)
        password += random.choice(capital_alphabets)
        password += random.choice(digits)
        password += random.choice(special_char)

        # Check if password contains repeated patterns
    while any(password[i:i+2] in password[i+2:] for i in range(len(password) - 2)):
        # if it does, generate a new password
        password = generate_password()

    # Check if password contains common phrases generated
    while any(phrase.lower() in password.lower() for phrase in COMMON_PHRASES_GENERATED):
        # lets say password "Omar"
        # common phrase "oma"
        password = generate_password()

    # Check if password contains common phrases
    while any(phrase.lower() in password.lower() for phrase in DICTIONARY):
        password = generate_password()

    # Check if password contains common names
    while any(name.lower() in password.lower() for name in NAMES):
        password = generate_password()

    print(password)
    password_checker(password)
    return password


def generate_password2():
    # generate password with at least 8 characters
    password = "".join(random.choice(
        small_alphabets + capital_alphabets + digits + special_char) for _ in range(8))

    # check if password has at least 1 lower and 1 upper and 1 digit and 1 special character
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_char = any(char in special_char for char in password)

    if not has_lower:
        lower_position = random.randint(0, len(password))
        password = password[:lower_position] + \
            random.choice(small_alphabets) + password[lower_position:]

    if not has_upper:
        upper_position = random.randint(0, len(password))
        password = password[:upper_position] + \
            random.choice(capital_alphabets) + password[upper_position:]

    # if password doesn't have digit, add one
    if not has_digit:
        # lets say password = "abcde"
        # generate random position between 0 and 5
        digit_position = random.randint(0, len(password))
        # lets say digit_position = 2
        password = password[:digit_position] + \
            random.choice(digits) + password[digit_position:]
        # password = "ab" + "1" + "cde"

    # if password doesn't have special character, add one
    if not has_special_char:
        special_char_position = random.randint(0, len(password))
        password = password[:special_char_position] + \
            random.choice(special_char) + password[special_char_position:]

    # Check if password contains repeated patterns
    while any(password[i:i+2] in password[i+2:] for i in range(len(password) - 2)):
        # if it does, generate a new password
        password = generate_password2()

    # Check if password contains common phrases generated
    while any(phrase.lower() in password.lower() for phrase in COMMON_PHRASES_GENERATED):
        # lets say password "Omar"
        # common phrase "oma"
        password = generate_password2()

    # Check if password contains common phrases
    while any(phrase.lower() in password.lower() for phrase in DICTIONARY):
        password = generate_password2()

    # Check if password contains common names
    while any(name.lower() in password.lower() for name in NAMES):
        password = generate_password2()

    print(password)
    # print("Password Length: ", len(password))
    password_checker(password)
    return password


method = input("Enter 1 to use method 1 or 2 to use method 2: ")
if method == "1":
    generate_password()
elif method == "2":
    generate_password2()
else:
    print("Invalid input")

while (input("Do you want to re-enter the password? (y/yes to continue): ") in ["y", "Y", "yes", "Yes"]):
    method = input("Enter 1 to use method 1 or 2 to use method 2: ")
    if method == "1":
        generate_password()
    elif method == "2":
        generate_password2()
    else:
        print("Invalid input")
print("Thank you for using our password generator")
