from bank_accounts import *


def atm_menu():
    print("Welcome to the ATM")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


def main():
    account = BankAccount(
        "1000", "Mswati"
    )  # Assuming BankAccount is a class from bank_accounts module
    while True:
        atm_menu()
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                print(f"Your current balance is: {account.balance}")
            case "2":
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            case "3":
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    account.viable_transaction(amount)
                    account.withdraw(amount)
                except BalanceException as error:
                    print(f"\nWithdraw interrupted: {error}")
                finally:
                    print("\nThank you for using the ATM.")

            case "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
