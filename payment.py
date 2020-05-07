from abc import ABC, abstractmethod
class Payment(ABC):
	@abstractmethod
	def make_payment(self , amount):
		pass
		
class Card(Payment):
	def make_payment(self , amount):
		print("Amount of {} is paid by card no ending with xxxxxxxx").format(amount)
		return amount
class UPI(Payment):
	def make_payment(self , amount):
		print("payment method is upi")
		return amount
	
	
class Cash(Payment):
	def make_payment(self , amount):
		print("payment by cash!!!!!")
		return amount
		
		
class PaymentFactory:
	@staticmethod
	def get_payment_type(payment_type):
		if payment_type == "Card":
			return Card()
		elif payment_type == "UPI":
			return UPI()
		else:
			return Cash()
if __name__ == "__main__":
	payment = PaymentFactory.get_payment_type(input())
	payment.make_payment(int(input()))
	
	
	

		

		

	
	

		

	
		


	