for n in range(5, 0, -1):
  print(n)
  
number = int(input('임의의 양수를 입력하세요 >>>'))
sum = 0

for n in range(1, number + 1):
  sum += n

print(f'1부터 {number}사이 모든 정수의 합계는 {sum}입니다.')

list = []
number = int(input('몇 개의 과일을 보관할까요? >>>'))
for n in range(1, number + 1):
  list.append(input(f'{n}번째 과일을 입력하세요 >>>'))

print(f'입력받은 과일들은 {list} 입니다.')


exam = [99, 78, 100, 91, 81, 85, 54, 100, 71, 50]
score = []

for ex in exam:
  score.append(min(100, ex + 5))
  
print(score)


for i in range(1, 100):
  display_text = str(i)
  
  if len(display_text) == 1:
    if display_text == '3' or display_text == '6' or display_text == '9':
      display_text = '짝'
  else:
    first_number = display_text[0:1]
    second_number = display_text[1:2]

    if first_number == '3' or first_number == '6' or first_number == '9':
      display_text = '짝'
    
    if second_number == '3' or second_number == '6' or second_number == '9':
      # 십의 자리가 3, 6, 9가 아니면 display_text 변수를 초기화 해준다.
      if display_text.isnumeric():
        display_text = ''
      
      # 십의 자리가 짝이면 짝짝이 되고, 십의 자리가 짝이 아니면 초기화를 해줬기 때문에 짝이 된다.
      display_text += '짝'


  if i % 10 == 0:
    if display_text == str(i):  
      print(i)
    else:
      print(display_text)
  else:
    if display_text == str(i):  
      print(f'{i}	', end='')
    else:
      print(f'{display_text}	', end='')