from panquetes.Payments.Payment import Payment

class CardPayment(Payment):
    def __init__(self, number, cvv):
        super().__init__()
        self.number = number
        self.cvv = cvv

    def pay(self, check):
        print(f"Paying ${check} with card {self.number[-4:]}")

class CashPayment(Payment):
    def __init__(self, get_money: float):
        super().__init__()
        self.money = get_money

    def pay(self, check):
        if self.money > check:
            print(f"It was paid the bill of ${check}, your change is ${self.money - check}")
        elif self.money == check:
            print(f"It was paid exact check, no change")
        else:
            print(f"You don't have enough money to pay the check, We accept other payment methods")
        