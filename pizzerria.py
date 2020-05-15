from abc import ABC , abstractmethod
class Pizzeria(ABC):
    @abstractmethod
    def order_pizza(self):
        pass
    @abstractmethod
    def wrap_pizza(self):
        pass
class Pizza(ABC):
    @abstractmethod
    def pizza_details(self):
        pass
    @abstractmethod
    def make_pizza(self):
        pass
class Hyd_Pizzeria(Pizzeria):
    @staticmethod
    def get_pizza_type(type):
        if type == "Cheese":
            return Cheese()
        elif type == "Margarita":
            return Margarita()
        elif type == "Veggies":
            return Veggies()
        elif type == "Chiken":
            return Chiken()
        else:
            return None
    def wrap_pizza(self):
        print("wrap pizza with a bucket of free haleem")
class Bang_Pizzeria(Pizzeria):
    @staticmethod
    def get_pizza_type(type):
        if type == "Margarita":
            return Margarita()
        elif type == "Cheese":
            return Cheese()
        else:
            return None
 
class Cheese(Pizza):
    def __init__(self):
        self.name = "Cheese"
        self.price = 100
    def make_pizza(self):
        print("cheese pizza ready")
    def pizza_details(self):
        return self.name , self.price
class Chiken(Pizza):
    def __init__(self):
        self.name = "Chiken"
        self.price = 300
    def make_pizza(self):
        print("Chiken Pizza Ready")
    def pizza_details(self):
        return self.name , self.price
class Margarita(Pizza):
    def __init__(self):
        self.name = "Margarita"
        self.price = 200
    def make_pizza(self):
        print("Margarita Ready")
    def pizza_details(self):
        return self.name , self.get_price
class Veggies(Pizza):
    def __init__(self):
        self.name = "Veggie"
        self.price = 200
    def make_pizza(self):
        print("Veg pizza ready!!!")
    def pizza_details(self):
        return self.name , self.price
 
def main(store , type):
    pizza = store.get_pizza_type(type)
    pizza.make_pizza()
    return pizza.pizza_details()
 
print(main(Hyd_Pizzeria , "Cheese"))
	
