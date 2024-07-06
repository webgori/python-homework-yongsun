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
  
  def __init__(self, oil, charge):
    super().__init__(oil)
    self.charge_value = charge
  
  def charge(self, charge):
    if charge <= 0:
      return
      
    self.charge_value += min(charge, Hybrid.max_charge)
  
  def hybrid_info(self):
    super().car_info()
    print(f'현재 충전상태: {self.charge_value}')
  
  
car = Hybrid(0, 0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()