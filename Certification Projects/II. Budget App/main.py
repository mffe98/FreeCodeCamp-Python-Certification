import math

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def deposit(self, amount, description = ''):
        self.add_to_ledger(amount, description)

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.add_to_ledger(-amount, description)
            return True
        return False

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction['amount']
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False
    
    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def add_to_ledger(self, amount, description):
        self.ledger.append(
            {
                'amount': amount,
                'description': description
            }
        )
    
    def __str__(self):
        num = round(15-len(self.name)/2)
        header = '*'*num + self.name.capitalize() + '*'*num + '\n'
        ledger_view = ''
        for transaction in self.ledger:
            desc = transaction['description'][:23]
            amt = transaction['amount'] 
            ledger_view += (desc.ljust(23, ' ') + f'{amt:.2f}'.rjust(7, ' ') + '\n')
        balance = f'Total: {self.get_balance():.2f}'
        return header + ledger_view + balance

def create_spend_chart(categories):
    header = 'Percentage spent by category\n'
    body = ''
    border = '    '+'---'*len(categories) + '-\n'
    footer = ''

    longest_name = 0
    withdrawal_history = {}
    for category in categories:
        total_spent = 0
        for trans in category.ledger:
            if trans['amount'] < 0:
                total_spent += abs(trans['amount'])
        withdrawal_history[category] = total_spent

        if longest_name < len(category.name):
            longest_name = len(category.name)

    overall_withdrawal_amt = sum([amount for amount in withdrawal_history.values()])

    percent_dict = {
    category: math.floor(amount / overall_withdrawal_amt * 10) * 10
    for category, amount in withdrawal_history.items()
    }

    for percent in range(100, -1, -10):
        y_axis = f'{percent}|'.rjust(4, ' ')

        for category, value in percent_dict.items():
            y_axis += ' o ' if value >= percent else '   '
        body += y_axis + ' \n'
    
    for index in range(longest_name):
        footer += '    '
        for category in categories:
            if index <= len(category.name) - 1:
                footer += ' ' + category.name[index] + ' ' 
            else:
                footer += '   '
        if index < longest_name - 1:
            footer += ' \n'
        else:
            footer += ' '

    return header + body + border + footer

