balance = 10000

while True:
  print(f'현재 {balance}원이 있습니다.')
  
  if balance == 0:
    break
  
  pay = int(input('사용할 금액 입력 >>>'))
  
  if pay > 0:
    if balance - pay < 0:
      print(f'{pay - balance}원이 부족합니다.')
    else:
      balance -= pay
  else:
    print('0 이하의 금액은 사용할 수 없습니다.')
    continue
  

while True:
  rating = int(input('이번 영화의 평점을 입력하세요 >>>'))
  
  if rating < 1 or rating > 5:
    print(f'평점은 1~5 사이만 입력할 수 있습니다.')
    continue
  else:
    print(f'평점: {'⭐' * rating}')
    break
  

password = 'qwerty'
correct = False

for count in range(1, 6):
  input_password = input('비밀번호를 입력하세요 >>>')
  
  if password == input_password:
    print('비밀번호를 맞혔습니다.')
    correct = True
    break
  
# correct가 False면
if not correct:
  print('비밀번호 입력 횟수를 초과했습니다.')
  
  
for dan in range(3, 10, 2):
  for n in range(1, dan + 1):
    print(f'{dan}x{n}={dan * n}')
    
  print('')