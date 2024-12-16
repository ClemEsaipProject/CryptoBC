from blockchain import Blockchain
from transaction import Transaction

def main():
    blockchain = Blockchain()

    while True:
        print("\n1. Add transaction")
        print("2. Check transaction")
        print("3. Show last 10 transactions")
        print("4. Tamper with transaction")
        print("5. Validate blockchain")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            sender = input("Enter sender: ")
            recipient = input("Enter recipient: ")
            amount = float(input("Enter amount: "))
            transaction = Transaction(sender, recipient, amount)
            transaction_id = blockchain.Add(transaction)
            print(f"Transaction added with ID: {transaction_id}")

        elif choice == '2':
            transaction_id = input("Enter transaction ID to check: ")
            transaction = blockchain.Check(transaction_id)
            if transaction:
                Transaction.display(transaction)
            else:
                print("Transaction not found.")

        elif choice == '3':
            transactions = blockchain.Show()
            for transaction in transactions:
                Transaction.display(transaction)
                print("---")

        elif choice == '4':
            transaction_id = input("Enter transaction ID to tamper with: ")
            if blockchain.Tamper(transaction_id):
                print("Transaction tampered successfully.")
            else:
                print("Transaction not found.")

        elif choice == '5':
            if blockchain.is_chain_valid():
                print("Blockchain is valid.")
            else:
                print("Blockchain is not valid.")

        elif choice == '6':
            blockchain.save_transactions()
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
