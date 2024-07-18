class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if not isinstance(amount, int) and not isinstance(amount, float): # fix saque recebe apenas valores inteiros ou fracionários
            return False
        
        if amount <= self.balance and amount >= 0: # fix : evitar saques sem sentido menores ou iguais a 0
            self.balance -= amount
            return True # fix : retorna true caso o saque seja realizado com sucesso
        else:
            print("Insufficient funds")
            return False # fix : retorna false caso o saque falhe

    def get_balance(self):
        return self.balance


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self):
        total_balance = 0
        for account in self.accounts:
            total_balance += account.get_balance()
        return total_balance


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def transfer(self, from_account, to_account, amount):
        if from_account.withdraw(amount):  # fix: condição necessária para averiguar possibilidade de saque
            to_account.deposit(amount)


def main():
    # Create a bank
    my_bank = Bank("MyBank")

    # Create customers
    alice = Customer("Alice", 1)
    bob = Customer("Bob", 2)

    # Add customers to the bank
    my_bank.add_customer(alice)
    my_bank.add_customer(bob)

    # Create accounts
    alice_account = Account("A001", 1000)
    bob_account = Account("B001", 500)

    # Add accounts to customers
    alice.add_account(alice_account)
    bob.add_account(bob_account)

    # Perform a transfer
    my_bank.transfer(alice_account, bob_account, 300.50)

    # Check balances
    print("Alice's balance:", alice_account.get_balance())
    print("Bob's balance:", bob_account.get_balance())


if __name__ == "__main__":
    main()