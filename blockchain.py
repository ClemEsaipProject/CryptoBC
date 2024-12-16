import json
import os
from block import Block
from transaction import Transaction
'''
###########################################class blockchain##################################################################
nous declarons en premier lieu les attributs dans la fonction _init_ puis nous ajoutons les focntions de genese de la chaine# 
et la focntion qui nous permet de nous retourner le block precedent(si il y en as un ), nous avons aussi les focntion comme #
l ajout du bloc dans la chaine des que 10 transaction sont faites                                                           #
la fonction qui cree un nouveau bloc dans la qui prend en compte le hash du bloc precedent , la fonction de verification,   #
 d'affichage, d'alteration et de validation                                                                                 #
la focntion de sauvegarde dans un fichier au format JSON nous permets de stocker les transaction et ainsi avoir un log ou   #
 repertoire qui vas nous servire pour apllication des fonction precedement enoncé                                           #
#############################################################################################################################    
'''
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.difficulty = 2
        self.load_transactions()

    def create_genesis_block(self):
        return Block([], "0")

    def get_latest_block(self):
        return self.chain[-1]

    def Add(self, transaction):
        self.pending_transactions.append(transaction)
        if len(self.pending_transactions) == 10:
            self.create_new_block()
        self.save_transactions()
        return transaction.id

    def create_new_block(self):
        new_block = Block(self.pending_transactions, self.get_latest_block().hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_transactions = []

    def Check(self, transaction_id):
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.id == transaction_id:
                    return transaction
        return None

    def Show(self):
        all_transactions = []
        for block in reversed(self.chain):
            all_transactions.extend(block.transactions)
        return all_transactions[:10]

    def Tamper(self, transaction_id):
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.id == transaction_id:
                    transaction.amount *= 2  
                    block.hash = block.calculate_hash()
                    return True
        return False

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def save_transactions(self):
        data = []
        for block in self.chain:
            for transaction in block.transactions:
                data.append(transaction.to_dict())
        
        with open('./transactions.json', 'w') as f:
            json.dump(data, f)

    def load_transactions(self):
        if not os.path.exists('./transactions.json'):
            return
        
        with open('./transactions.json', 'r') as f:
            data = json.load(f)
        
        for transaction_data in data:
            transaction = Transaction.from_dict(transaction_data)
            self.Add(transaction)
