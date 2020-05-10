class House:
  def __init__(self , builder):
    self.mk = builder.mk
    self.roof = builder.roof
    self.door = builder.door
    self.window = builder.window
  class Builder:
    def __init__(self , roof , window , door):
      self.roof = roof
      self.window = window
      self.door = door
    def build_modular_kitchen(self , mk):
      self.mk = mk
      return self
	def installing_heating_system(self , hs):
		self.hs = hs
		return self
	def building_balcony(self , bal):
		self.bal = bal
		return self
	def wooden_flooring(self , wf):
		self.wf = wf
		return wf
    def build(self):
      house = House(self)
      return house
    
def main():
  hw = House.Builder(True , True , True).building_modular_kitchen(True).installing_heating_system().building_balcony().build()
  return hw.mk , hw.roof ,hw.window , hw.door

print(main()))