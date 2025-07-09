from abc import ABC, abstractmethod
class PaymenProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class Paypal(PaymenProcessor):
    def pay(self, amount):
        print(f'Оплата {amount} руб через PayPal')

class CreditCard(PaymenProcessor):
    def pay(self, amount):
        print(f'Оплата {amount} руб через CreditCard')


class Crypto(PaymenProcessor):
    def pay(self, amount):
        print(f'Оплата {amount} руб через Crypto')


def process_payment(payment_processor: PaymenProcessor, amount: float):
    payment_processor.pay(amount)


paypal = Paypal()
creditcard = CreditCard()
crypto = Crypto()
process_payment(paypal, 1000)
process_payment(creditcard, 3000)
process_payment(crypto, 5000)




