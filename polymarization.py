class Payment:
    def pay(self):
        print("Processing payment")

class CreditCard(Payment):
    def pay(self):
        print("Payment done using Credit Card")

class UPI(Payment):
    def pay(self):
        print("Payment done by UPI")

class Cash(Payment):
    def pay(self):
        print("Payment done by Cash")

p1 = CreditCard()
p2 = UPI()
p3 = Cash()

p1.pay()
p2.pay()
p3.pay()