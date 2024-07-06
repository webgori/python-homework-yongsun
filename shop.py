class Shop():
  total = 0
  menu_list = [{'떡볶이': 3000}, {'순대': 3000}, {'튀김': 500}, {'김밥': 2000}]
  
  @classmethod
  def sales(cls, menu, count):
    for menu_dict in cls.menu_list:
      for key in menu_dict:
        if menu == key:
          cls.total += (menu_dict[key] * count)
          break
        
shop = Shop()
shop.sales('떡볶이', 1)
shop.sales('김밥', 2)
shop.sales('튀김', 5)

print('매출: {}원'.format(Shop.total))