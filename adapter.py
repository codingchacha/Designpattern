class UsMotorsAbstract(ABC):
    @abstractmethod
    def speed_in_miles(self , distance , time):
        pass
class Usmotors(UsMotorsAbstract):
    def speed_in_miles(self , distance , time):
        print("returning speed in miles")
        return distance // time
class IndianMotorAbstract(ABC):
    @abstractmethod
    def speed_in_km(self):
        pass
class IndianMotors(IndianMotorAbstract):
    def speed_in_km(self , distance , time):
        print("returning speed in kilometer")
        return distance // time
class SpeedAdapter(UsMotorsAbstract):
    def __init__(self , obj):
        self.obj = obj
    def speed_in_miles(self , distance , time):
        result = self.obj.speed_in_km(distance , time)
        return result
def main():
    im = IndianMotors()
    speedadapter = SpeedAdapter(im)
    result = speedadapter.speed_in_miles(10 , 2)
    print(result)
main()