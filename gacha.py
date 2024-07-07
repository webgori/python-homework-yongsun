from random import randint

class Gacha:
  products_name = [
    '빽다방 1,000원 할인권',
    '빽다방 2,000원 할인권',
    '빽다방 3,000원 할인권',
    '빽다방 아메리카노 1잔 교환권',
    '빽다방 아메리카노 2잔 교환권',
    ]

  products_rate = [
    [37, 25, 20],
    [32, 33, 33],
    [25, 33, 33],
    [5, 7, 11],
    [1, 2, 3]
    ]

  price_1000_products = ['빽다방 1,000원 할인권', '빽다방 1,000원 할인권', '빽다방 1,000원 할인권', '빽다방 1,000원 할인권', '빽다방 2,000원 할인권', '빽다방 2,000원 할인권', '빽다방 2,000원 할인권', '빽다방 3,000원 할인권', '빽다방 3,000원 할인권', '빽다방 아메리카노 1잔 교환권', '빽다방 아메리카노 1잔 교환권', '빽다방 아메리카노 2잔 교환권']
  price_2000_products = ['빽다방 1,000원 할인권', '빽다방 1,000원 할인권', '빽다방 1,000원 할인권', '빽다방 2,000원 할인권', '빽다방 2,000원 할인권', '빽다방 2,000원 할인권', '빽다방 3,000원 할인권', '빽다방 3,000원 할인권', '빽다방 아메리카노 1잔 교환권', '빽다방 아메리카노 1잔 교환권', '빽다방 아메리카노 1잔 교환권', '빽다방 아메리카노 2잔 교환권']
  price_3000_products = ['빽다방 1,000원 할인권', '빽다방 1,000원 할인권', '빽다방 2,000원 할인권', '빽다방 2,000원 할인권', '빽다방 3,000원 할인권', '빽다방 3,000원 할인권', '빽다방 아메리카노 1잔 교환권', '빽다방 아메리카노 1잔 교환권', '빽다방 아메리카노 1잔 교환권', '빽다방 아메리카노 2잔 교환권', '빽다방 아메리카노 2잔 교환권', '빽다방 아메리카노 2잔 교환권']

  def __init__(self):
    self.mode = 'guest'
    self.command = ''
    self.admin_password = 'admin'
    self.balance = 10000
    self.buy_list = []
    self.total_sales = 0
    self.running = True

  def run(self):
    while self.running:
      if self.mode == 'guest':
        self.input_guest()
      elif self.mode == 'admin':
        self.input_admin()
        
      self.command_action()


  def input_guest(self):
    self.command = input('손님: 명령을 입력하세요 (a: 관리자 모드, 1: 1,000원 상품 구매, 2: 2,000원 상품 구매, 3: 3,000원 상품 구매, b: 현재 잔액 조회, l: 현재 구매한 상품 목록 조회) >>> ')

  def input_admin(self):
    self.command = input('관리자: 명령을 입력하세요 (g: 손님 모드, p: 매출 조회) >>> ')
    
  def command_action(self):
    if self.command == 'a':
      self.admin_mode()
    elif self.command == '1':
      self.buy(1000)
    elif self.command == '2':
      self.buy(2000)
    elif self.command == '3':
      self.buy(3000)
    elif self.command == 'b':
      self.print_balance()
    elif self.command == 'l':
      self.print_buy_list()
    elif self.command == 'g':
      self.guest_mode()
    elif self.command == 'p':
      self.print_total_sales()
      

  def admin_mode(self):
    admin = self.check_admin_password()

    if admin:
      self.mode = 'admin'
    

  def check_admin_password(self):
    password = input('비밀번호를 입력하세요 >>> ')
    
    if password != self.admin_password:
      print('비밀번호가 올바르지 않습니다.')
      return False
    
    return True
    

  def get_product(self, price):
    sum_rate = 0
    random_value = randint(1, 100)
    rate_index = 0

    if price == 1000:
      rate_index = 0
    elif price == 2000:
      rate_index = 1
    elif price == 3000:
      rate_index = 2
    
    for products_rate_index, rate_list in enumerate(self.products_rate):
      rate = rate_list[rate_index]

      sum_rate += rate

      if sum_rate >= random_value:
        return self.products_name[products_rate_index], rate

  def buy(self, price):
    buyable = self.check_balance(price)
    
    if buyable == False:
      return
    
    '''
    global price_1000_products
    shuffle(price_1000_products)

    random_product = price_1000_products[0]
    
    rate = get_product_rate(price_1000_products, random_product)
    '''

    random_product, rate = self.get_product(price)

    print(f'{random_product} 상품이 나왔습니다! ({rate}% 확률)')

    self.buy_list.append(random_product)
    self.total_sales += price
    self.balance -= price
    
    self.check_exit_program()
    
  def check_balance(self, price):
    if price > self.balance:
      print(f'잔액이 부족합니다. 잔액: {self.balance}, 상품 금액 {price}')
      return False
    
    return True

  '''
  def get_product_rate(self, products, product_name):
    product_count = 0

    for product in products:
      if product == product_name:
        product_count += 1

    return round(product_count / len(products) * 100, 2)
  '''

  def print_balance(self):
    print(f'현재 잔액은 {self.balance}원 입니다.')
    
  def print_buy_list(self):
    global buy_list
    
    print(f'총 구매 상품: {self.buy_list}')
    
  def print_total_sales(self):
    print(f'오늘의 총 매출은 {self.total_sales}원 입니다.')
    
  def guest_mode(self):
    self.mode = 'guest'

  def check_exit_program(self):
    if self.balance == 0:
      print('잔액이 부족하여 더이상 구매할 수 있는 상품이 없으므로 프로그램을 종료합니다.')
      self.running = False


gacha = Gacha()
gacha.run()