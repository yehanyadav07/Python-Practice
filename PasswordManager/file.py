import random
import string

passwords = {}

# Load saved passwords
try:
    with open("passwords.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwords[website] = pwd
except FileNotFoundError:
    pass


# Function to generate password
def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = "".join(random.choice(chars) for _ in range(10))
    return password


while True:
    print("\n===== PERSONAL PASSWORD MANAGER =====")
    print("1. Save Password")
    print("2. View Passwords")
    print("3. Generate Password")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Save Password
    if choice == "1":
        site = input("Enter website name: ")

        ask = input("Generate password? (yes/no): ").lower()

        if ask == "yes":
            pwd = generate_password()
            print("Generated Password:", pwd)
        else:
            pwd = input("Enter password: ")

        passwords[site] = pwd

        with open("passwords.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")

        print("Password saved successfully!")

    # View Passwords
    elif choice == "2":
        if not passwords:
            print("No passwords saved.")
        else:
            print("\nSaved Passwords:")
            print("-" * 30)
            for site, pwd in passwords.items():
                print(f"{site} : {pwd}")

    # Generate Password
    elif choice == "3":
        print("Generated Password:", generate_password())

    # Exit
    elif choice == "4":
        print("Thank you for using Password Manager!")
        break

    else:
        print("Invalid choice. Please try again.")