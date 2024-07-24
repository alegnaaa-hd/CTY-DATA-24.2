

class CreditCard:


    def __init__(self):
        self.name = ""
        self.card_no = 0
        self.exp_date = ""
        self.cvv = 0
        self.type = ""
        self.credit_limit = 0.0
        self.balance = 0.0
        self.next = None

    def display_card_infos(self):

        print("--------------------------------")
        print("Credit Card No: ", self.card_no)
        print("Customer Name: ", self.name)
        print("Expiration Date: ", self.exp_date)
        print("CVV: ", self.cvv)
        print("Card Type: ", self.type)
        print("Credit Limit: $", self.credit_limit)
        print("Credit Card Balance: $", self.balance)
        print("--------------------------------")
    

class DoubleLinkedCard(CreditCard):

    def __init__(self):
        super().__init__()
        self.previous = None 

