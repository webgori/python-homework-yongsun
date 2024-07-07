class Car():
  max_oil = 50
  
  def __init__(self, oil):
    self.oil = oil
    
  def add_oil(self, oil):
    if oil <= 0:
      return
    
    self.oil += oil
    
    if self.oil > Car.max_oil:
      self.oil = Car.max_oil
      
  def car_info(self):
    print('현재 주유상태: {}'.format(self.oil))
    
  
class Hybrid(Car):
  max_charge = 30
  
  def __init__(self, oil, charge_value):
    super().__init__(oil)
    self.battery = charge_value
  
  def charge(self, charge_value):
    if charge_value <= 0:
      return
      
    self.battery += min(charge_value, Hybrid.max_charge)
  
  def hybrid_info(self):
    super().car_info()
    print(f'현재 충전상태: {self.battery}')
  
  
car = Hybrid(0, 0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()