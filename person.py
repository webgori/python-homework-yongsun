class Person():
  population = 0
  
  def __init__(self, name):
    self.name = name
    print(f'{name} is born')
    
    Person.population += 1
    
  def __del__(self):
    print(f'{self.name} is dead.')
    Person.population -= 1
    
  @classmethod
  def get_population(cls):
    return cls.population

man = Person('james')
woman = Person('emily')

print('전체 인구수: {}명'.format(Person.get_population()))

del man

print('전체 인구수: {}명'.format(Person.get_population()))