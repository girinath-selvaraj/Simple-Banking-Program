#banking

def show_banalce(balance):
    print(f"Available balance is Rs.{balance:.2f}")

def deposit():
    amount = float(input("Enter amount to deposit: "))
    if amount < 0:
        print("Enter Valid Amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter Amount to Withdraw:"))

    if amount > balance:
        print("Insufficient Balance")
        return 0
    elif amount < 0:
        print("Amount not less then 0")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("###############################")
        print("Welcome to the Banking Program!")
        print("###############################")
        print("1.View Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        print("###############################")

        choice = input("Enter your choice(1-4): ")

        if choice == "1":
            show_banalce(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for Banking with us!")

if __name__ == '__main__':
    main()