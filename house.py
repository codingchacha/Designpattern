class House:
  def build_roof(self):
    print("roof is set")
  def install_door(self):
    print("door is installed")
  def fix_window_pair(self):
    print("windows pair fixed")
  class Builder:
    def build_modular_kitcher(self):
      print("kithen modular built")
      return self
    def get_heating_system(self):
      print("heating system installed in this house")
      return self
    def wooden_floor(self):
      print("wooden floor installed in this house")
      return self
    def make_balcony(self):
      print("This house has balcony")
      return self
    def build(self):
      house = House(self)
      return house
  builder = Builder()
house = House()
house.builder.get_heating_system().build_modular_kitcher()