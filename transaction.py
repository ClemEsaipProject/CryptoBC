import hashlib
import time

'''
###########################################class transaction#################################################################
nous declarons en premier lieu les attributs dans la fonction _init_ , puis la focntion de hash de la transaction qui vas   #
 nous servir dans la creation d'un bloc                                                                                     #
#############################################################################################################################    
'''


class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = time.time()
        self.id = self.calculate_hash()

    def calculate_hash(self):
        transaction_string = f"{self.sender}{self.recipient}{self.amount}{self.timestamp}"
        return hashlib.sha256(transaction_string.encode()).hexdigest()

    @staticmethod
    def display(transaction):
        print(f"ID: {transaction.id}")
        print(f"From: {transaction.sender}")
        print(f"To: {transaction.recipient}")
        print(f"Amount: {transaction.amount}")
        print(f"Timestamp: {transaction.timestamp}")

    def to_dict(self):
        return {
            'id': self.id,
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'timestamp': self.timestamp
        }

    @classmethod
    def from_dict(cls, data):
        transaction = cls(data['sender'], data['recipient'], data['amount'])
        transaction.id = data['id']
        transaction.timestamp = data['timestamp']
        return transaction
