number = int(input('정수를 입력하세요 >>>'))

if number <= 0:
  print('잘못된 입력입니다.')
else:
  count = 1
  while number >= count:
    print(f'{count}번째 Hello')
    count += 1
    
count = 1
while count <= 100:
  if count % 7 == 0:
    print(count)
  count += 1
  

coin = int(input('자판기에 얼마를 넣을까요? >>>'))

coffee_cost = 300
count = 1
coffee_count = coin // coffee_cost

while count <= coffee_count:
  coffee_jandon = coin - (count * coffee_cost)
  print(f'커피 {count}잔, 잔돈 {coffee_jandon}원')
  count += 1
  
  
number_set = set()

while len(number_set) != 5:
  number = int(input('0 ~ 9 사이 정수를 입력하세요 >>>'))
  number_set.add(number)

print('모두 입력되었습니다.')
print(f'입력된 값은 {number_set} 입니다.')

count = 1

while count <= 100:
  line = ''
  count2 = 1
  
  while count2 <= 10:
    line += f'{str(count)}	'
    count += 1
    count2 += 1
  
  print(line)
  

n = 1

while n <= 9:
  line = ''
  dan = 2
  
  while dan <= 9:
    line += f'{dan}x{n}={dan*n}	'
    dan += 1
  
  print(line)
  n += 1