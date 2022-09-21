class Money:

    CURRENCY = '₹'

    CURRENCY_VALUES = {
        "20's Note": 20,
        "10's Note/Coin": 10,
        "5's Note/Coin": 5,
        "2's Coin": 2,
        "1's Coin": 1
    }

    def __init__(self):
        self.profit = 0
        

    def report(self):
        '''Prints the current profit'''
        print(f'Money: {self.CURRENCY}{self.profit}')


    def process_money(self):
        '''Returns the total calculatoed from Notes/Coins inserted'''
        print("Please insert Notes/Coins.")
        money_received = 0
        for currency in self.CURRENCY_VALUES:
            money_received += int(input(f"How many {currency}?:")) * self.CURRENCY_VALUES[currency]

        return money_received

    def make_payment(self, cost):
        '''Returns True if the payment accepted or return False'''
        money_received = self.process_money()
        if money_received >= cost:
            change = round(money_received - cost, 2)
            print(f'Here is {self.CURRENCY}{change} in change.')
            self.profit += cost 
            return True 
        else:
            print("Not enough money! Money refunded")
            return False