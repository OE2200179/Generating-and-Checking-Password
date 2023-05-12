capital_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_alphabets = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
special_char = "!@#$%^&*()-+"


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


# take input from user
password = input("Enter the password: ")
password_checker(password)
while (input("Do you want to re-enter the password? (y/yes to continue): ") in ["y", "Y", "yes", "Yes"]):
    password = input("Re-enter the password: ")
    password_checker(password)
print("Thank you for using password checker.")
