import time

print("Please insert Your CARD")

time.sleep(5)

password = 1234

# Loop until the correct PIN is entered
while True:
    try:
        pin = int(input("Enter your ATM PIN: "))
        if pin == password:
            break
        else:
            print("Incorrect PIN. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numerical PIN.")

balance = 5000

while True:
    print("""
    1 == Check balance
    2 == Withdraw balance
    3 == Deposit balance
    4 == Exit
    """)

    try:
        option = int(input("Please enter your choice: "))
    except ValueError:
        print("Please enter a valid option.")
        continue

    if option == 1:
        print(f"Your current balance is {balance}")
        print("-----------------------------------------------------------------------------------------------------------------------")

    elif option == 2:
        try:
            withdraw_amount = int(input("Please enter withdraw amount: "))
            if withdraw_amount > balance:
                print("Insufficient balance.")
            else:
                balance -= withdraw_amount
                print(f"{withdraw_amount} is debited from your account")
                print(f"Your current balance is {balance}")
        except ValueError:
            print("Please enter a valid amount.")
        print("-----------------------------------------------------------------------------------------------------------------------")

    elif option == 3:
        try:
            deposit_amount = int(input("Please enter deposit amount: "))
            balance += deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"Your updated balance is {balance}")
        except ValueError:
            print("Please enter a valid amount.")
        print("-----------------------------------------------------------------------------------------------------------------------")

    elif option == 4:
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
        print("-----------------------------------------------------------------------------------------------------------------------")
