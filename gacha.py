mode = 'guest'
command = ''
admin_password = 'admin'
balance = 10000
buy_list = []
sold_products = []
running = True
price_1000_products = ['', '', '', '', '', '', '', '', '', '무선 마우스']
price_2000_products = ['', '', '', '', '', '', '', '', '', '기계식 키보드']
price_3000_products = ['', '', '', '', '', '', '', '', '', '그래픽 카드']

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
  
  print('1000원 상품 구매')
  
  global balance
  balance -= 1000
  
  check_exit_program()
  
def buy_2000():
  buyable = check_balance(2000)
  
  if buyable == False:
    return
  
  print('2000원 상품 구매')
  
  global balance
  balance -= 2000
  
  check_exit_program()
  
def buy_3000():
  buyable = check_balance(3000)
  
  if buyable == False:
    return
  
  print('3000원 상품 구매')
  
  global balance
  balance -= 3000
  
  check_exit_program()
  
def check_balance(price):
  global balance
  
  if price > balance:
    print(f'잔액이 부족합니다. 잔액: {balance}, 상품 금액 {price}')
    return False
  
  return True

def print_balance():
  global balance
  print(f'현재 잔액은 {balance}원 입니다.')
  
def print_buy_list():
  global buy_list
  
  print(f'총 구매 상품: {buy_list}')
  
def print_total_sales():
  print(f'오늘의 매출은 총 {get_total_sales()}원 입니다.')
  
def get_total_sales():
  global sold_products
  total_sales = 0
  
  for sold_product in sold_products:
    for sold_product_key in sold_product:
      total_sales += sold_product[sold_product_key]
      
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