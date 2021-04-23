class Category:
    def __init__(self, category, amount):
        self.category = str(category)
        try:
            self.amount = int(amount)
        except ValueError:
            print('Please enter an integer for the budget. It has been set to 0.')
            self.amount = 0

    #methods
    def deposit(self, modified_amount):
        try:
            self.amount = self.amount + int(modified_amount)
            message = 'The new balance for ' + self.category + ' is: ' + str(self.amount)
            return message
        except ValueError:
            return 'Please enter an integer to deposit.'

    def check_balance(self):
        message = 'The current balance for ' + self.category + ' is: ' + str(self.amount)
        return message

    def withdraw(self, modified_amount):
        try:
            self.amount = self.amount - int(modified_amount)
            message = 'The new balance for ' + self.category + ' is: ' + str(self.amount)
            return message
        except ValueError:
            return 'Please enter an integer to withdraw.'

    def transfer(self, transfer_amount, instance):
        try:
            self.amount = self.amount - int(transfer_amount)

            try:
                instance.deposit(transfer_amount)
                message = 'The new balance for ' + self.category + ' is: ' + str(self.amount) + '.\n' + instance.check_balance()
                return message
            except:
                return 'Please choose an existing category to transfer.'

        except ValueError:
            return 'Please enter an integer to transfer.'
        


clothing = Category('Clothing', 1000) 
food = Category('Food', 1000) 
car_expenses = Category('Car Expenses', 1000)


