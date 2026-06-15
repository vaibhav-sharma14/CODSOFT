import random
import string

print("\n------WELCOME TO RANDOM PASSWORD GENERATOR------\n")

length = int(input("Please Enter The Length Of The Password: "))

print("1. Letters Only")
print("2. Letters and Numbers")
print("3. Letters, Numbers and Symbols")

choice = input("Please Enter Your Choice For Your Password: ")

if choice == "1":

    chars = string.ascii_letters
    password = ""

    for i in range(length):
        password += random.choice(chars)

elif choice == "2":

    if length < 2:
        print("Password length must be at least 2")
        exit()

    chars = string.ascii_letters + string.digits

    password = random.choice(string.digits)

    for i in range(length - 1):
        password += random.choice(chars)

    password = ''.join(random.sample(password, len(password)))

elif choice == "3":

    if length < 3:
        print("Password length must be at least 3")
        exit()

    chars = string.ascii_letters + string.digits + string.punctuation

    password = (
        random.choice(string.ascii_letters)
        + random.choice(string.digits)
        + random.choice(string.punctuation)
    )

    for i in range(length - 3):
        password += random.choice(chars)

    password = ''.join(random.sample(password, len(password)))

else:
    print("Invalid Choice")
    exit()

print("\nYour Generated Password is:",password)

if length <= 5:
    print("Password Strength: Weak")

elif length <= 10:
    print("Password Strength: Medium")

else:
    print("Password Strength: Strong")
