class Wallet:

    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance
    
    def view_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return  f'you deposited {amount} your balance is {self.balance}'
    
def firstuser():
    mywallet = Wallet("Ishmo", 100000000)
    message = mywallet.deposit(200000000)
    return message
