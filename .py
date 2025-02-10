
    Account = BankAccount()

    While True:
        Print(“\n1. Deposit”)
        Print(“2. Withdraw”)
        Print(“3. Check Balance”)
        Print(“4. Exit”)

        Choice = input(“Enter choice: “)

        If choice == ‘1’:
            Amount = float(input(“Enter deposit amount: “))
            Account.deposit(amount)
        Elif choice == ‘2’:
            Amount = float(input(“Enter withdrawal amount: “))
            Account.withdraw(amount)
        Elif choice == ‘3’:
            Account.check_balance()
        Elif choice == ‘4’:
            Break
        Else:
            Print(“Invalid choice. Please try again.”)
