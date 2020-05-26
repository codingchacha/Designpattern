class Home:
    def get_cost(self):
        return 200000
class Plaster(Home):
    def __init__(self , wrapper):
        self.wrapper = wrapper
    def get_cost(self):
        return 10000 + self.wrapper.get_cost()
class Painting(Home):
    def __init__(self , wrapper):
        self.wrapper = wrapper
    def get_cost(self):
        return 5000 + self.wrapper.get_cost()
class Marble_Flooring(Home):
    def __init__(self , wrapper):
        self.wrapper = wrapper
    def get_cost(self):
        return 50000 + self.wrapper.get_cost()
 
class AirConditioner(Home):
    def __init__(self , wrapper):
        self.wrapper = wrapper
    def get_cost(self):
        return 15000 + self.wrapper.get_cost()
home = Home()
total_cost = Plaster(Painting(Marble_Flooring(AirConditioner(home))))
print(total_cost.get_cost())