'''
for n in range(5, 0, -1):
  print(n)
  
number = int(input('임의의 양수를 입력하세요 >>>'))
sum = 0

for n in range(1, number + 1):
  sum += n

print(f'1부터 {number}사이 모든 정수의 합계는 {sum}입니다.')

list = []
number = int(input('몇 개의 과일을 보관할까요? >>>'))
for n in range(1, 5 + 1):
  list.append(input(f'{n}번째 과일을 입력하세요 >>>'))

print(f'입력받은 과일들은 {list} 입니다.')


exam = [99, 78, 100, 91, 81, 85, 54, 100, 71, 50]
score = []

for ex in exam:
  score.append(min(100, ex + 5))
  
print(score)
'''


for i in range(1, 100):
  clap = str(i)
  
  if len(clap) == 1:
    if clap == '3' or clap == '6' or clap == '9':
      clap = '짝'
  else:
    first_number = clap[0:1]
    second_number = clap[1:2]

    if first_number == '3' or first_number == '6' or first_number == '9':
      clap = '짝'
    
    if second_number == '3' or second_number == '6' or second_number == '9':
      if clap.isnumeric():
        clap = ''
      clap += '짝'


  if i % 10 == 0:
    if clap == str(i):  
      print(i)
    else:
      print(clap)
  else:
    if clap == str(i):  
      print(f'{i}	', end='')
    else:
      print(f'{clap}	', end='')
  
  '''
  for j in range(1, 10):
    line += f'{i}	'
  print(line)
  '''