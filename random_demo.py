import random
from getpass import getpass
from pwinput import pwinput

# ring='ibguiefvbiebvfiebufvieufvihvuighviruvhirhtvihurbihubigu'
# lists=[1,2,3,4,5,6,7,8,9]
# a=list(ring)+lists

# print(random.choice(a))




balance = float(input("Enter initial balance: "))
correct_pin = input("Set your ATM PIN: ")

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            pin = pwinput("Enter your PIN: ")

            if pin == correct_pin:
                print("Your balance is:", balance)
            else:
                print("Incorrect PIN!")

        case 2:
            pin = pwinput("Enter your PIN: ")

            if pin == correct_pin:
                amount = float(input("Enter deposit amount: "))

                if amount > 0:
                    balance += amount
                    print("Deposit successful!")
                    print("Current balance:", balance)
                else:
                    print("Invalid deposit amount!")
            else:
                print("Incorrect PIN!")

        case 3:
            pin = pwinput("Enter your PIN: ")

            if pin == correct_pin:
                amount = float(input("Enter withdrawal amount: "))

                if amount <= 0:
                    print("Invalid withdrawal amount!")
                elif amount <= balance:
                    balance -= amount
                    print("Withdrawal successful!")
                    print("Remaining balance:", balance)
                else:
                    print("Insufficient balance!")
            else:
                print("Incorrect PIN!")

        case 4:
            print("Thank you for using the ATM!")
            break

        case _:
            print("Invalid choice! Please select 1-4.")
