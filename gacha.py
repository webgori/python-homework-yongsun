from random import shuffle

mode = 'guest'
command = ''
admin_password = 'admin'
balance = 10000
buy_list = []
total_sales = 0
running = True
price_1000_products = ['빽다방 1,000원 할인권', '빽다방 1,000원 할인권', '빽다방 1,000원 할인권', '빽다방 1,000원 할인권', '빽다방 2,000원 할인권', '빽다방 2,000원 할인권', '빽다방 2,000원 할인권', '빽다방 3,000원 할인권', '빽다방 3,000원 할인권', '빽다방 아메리카노 1잔 교환권', '빽다방 아메리카노 1잔 교환권', '빽다방 아메리카노 2잔 교환권']

price_2000_products = ['빽다방 1,000원 할인권', '빽다방 1,000원 할인권', '빽다방 1,000원 할인권', '빽다방 2,000원 할인권', '빽다방 2,000원 할인권', '빽다방 2,000원 할인권', '빽다방 3,000원 할인권', '빽다방 3,000원 할인권', '빽다방 아메리카노 1잔 교환권', '빽다방 아메리카노 1잔 교환권', '빽다방 아메리카노 1잔 교환권', '빽다방 아메리카노 2잔 교환권']

price_3000_products = ['빽다방 1,000원 할인권', '빽다방 1,000원 할인권', '빽다방 2,000원 할인권', '빽다방 2,000원 할인권', '빽다방 3,000원 할인권', '빽다방 3,000원 할인권', '빽다방 아메리카노 1잔 교환권', '빽다방 아메리카노 1잔 교환권', '빽다방 아메리카노 1잔 교환권', '빽다방 아메리카노 2잔 교환권', '빽다방 아메리카노 2잔 교환권', '빽다방 아메리카노 2잔 교환권']

def input_guest():
  global command
  command = input('손님: 명령을 입력하세요 (a: 관리자 모드, 1: 1,000원 상품 구매, 2: 2,000원 상품 구매, 3: 3,000원 상품 구매, b: 현재 잔액 조회, l: 현재 구매한 상품 목록 조회) >>> ')

def input_admin():
  global command
  command = input('관리자: 명령을 입력하세요 (g: 손님 모드, p: 매출 조회) >>> ')
  
def command_action():
  global command
  
  if command == 'a':
    admin_mode()
  elif command == '1':
    buy_1000()
  elif command == '2':
    buy_2000()
  elif command == '3':
    buy_3000()
  elif command == 'b':
    print_balance()
  elif command == 'l':
    print_buy_list()
  elif command == 'g':
    guest_mode()
  elif command == 'p':
    print_total_sales()
    

def admin_mode():
  check_admin_password()
  
  global mode
  mode = 'admin'

def check_admin_password():
  global admin_password
  
  password = input('비밀번호를 입력하세요 >>> ')
  
  if password != admin_password:
    print('비밀번호가 올바르지 않습니다.')
    return
  
def buy_1000():
  buyable = check_balance(1000)
  
  if buyable == False:
    return
  
  global price_1000_products
  shuffle(price_1000_products)

  random_product = price_1000_products[0]
  
  rate = get_product_rate(price_1000_products, random_product)
  print(f'{random_product} 상품이 나왔습니다! ({rate}% 확률)')

  global buy_list
  buy_list.append(random_product)

  global total_sales
  total_sales += 1000
  
  global balance
  balance -= 1000
  
  check_exit_program()
  
def buy_2000():
  buyable = check_balance(2000)
  
  if buyable == False:
    return
  
  global price_2000_products
  shuffle(price_2000_products)

  random_product = price_2000_products[0]
  
  rate = get_product_rate(price_2000_products, random_product)
  print(f'{random_product} 상품이 나왔습니다! ({rate}% 확률)')

  global buy_list
  buy_list.append(random_product)

  global total_sales
  total_sales += 2000
  
  global balance
  balance -= 2000
  
  check_exit_program()
  
def buy_3000():
  buyable = check_balance(3000)
  
  if buyable == False:
    return
  
  global price_3000_products
  shuffle(price_3000_products)

  random_product = price_3000_products[0]
  
  rate = get_product_rate(price_3000_products, random_product)
  print(f'{random_product} 상품이 나왔습니다! ({rate}% 확률)')

  global buy_list
  buy_list.append(random_product)

  global total_sales
  total_sales += 3000
  
  global balance
  balance -= 3000
  
  check_exit_program()
  
def check_balance(price):
  global balance
  
  if price > balance:
    print(f'잔액이 부족합니다. 잔액: {balance}, 상품 금액 {price}')
    return False
  
  return True

def get_product_rate(products, product_name):
  product_count = 0

  for product in products:
    if product == product_name:
      product_count += 1

  return round(product_count / len(products) * 100, 2)

def print_balance():
  global balance
  print(f'현재 잔액은 {balance}원 입니다.')
  
def print_buy_list():
  global buy_list
  
  print(f'총 구매 상품: {buy_list}')
  
def print_total_sales():
  print(f'오늘의 총 매출은 {get_total_sales()}원 입니다.')
  
def get_total_sales():
  global total_sales
  return total_sales
  
def guest_mode():
  global mode
  mode = 'guest'

def check_exit_program():
  global balance
  
  if balance == 0:
    print('잔액이 부족하여 더이상 구매할 수 있는 상품이 없으므로 프로그램을 종료합니다.')
    global running
    running = False

while running:
  if mode == 'guest':
    input_guest()
  elif mode == 'admin':
    input_admin()
    
  command_action()