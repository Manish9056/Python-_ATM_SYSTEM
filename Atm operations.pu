from atm.account import balance, transactions

def show_balance():
    print(f"\nCurrent Balance: ₹{balance}")


def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))

    if amount <= 0:
        print("Invalid amount!")
        return

    balance += amount
    transactions.append(f"Deposited ₹{amount}")

    print(f"₹{amount} deposited successfully!")


def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount!")
        return

    if amount > balance:
        print("Insufficient balance!")
        return

    balance -= amount
    transactions.append(f"Withdrew ₹{amount}")

    print(f"₹{amount} withdrawn successfully!")


def show_statement():
    print("\n===== TRANSACTION STATEMENT =====")

    if not transactions:
        print("No transactions yet.")
        return

    for i, t in enumerate(transactions, start=1):
        print(f"{i}. {t}")
