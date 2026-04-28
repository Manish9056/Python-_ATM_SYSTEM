from atm.operations import show_balance, deposit, withdraw, show_statement

def menu():
    print("\n====== ATM MENU ======")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Statement")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        show_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        show_statement()
    elif choice == "5":
        print("Thank you for using ATM!")
        break
    else:
        print("Invalid choice! Try again.")
