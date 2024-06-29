def vending_machine(money):
  drink_cost = 700
  drink_count = money // drink_cost
  
  for i in range(0, drink_count + 1):
    jandon = money - (i * drink_cost)
    print(f'음료수 = {i}개, 잔돈 = {jandon}원')
    
vending_machine(3000)



def get_average(marks):
  sum = 0
  
  for key in marks:
    score = marks[key]
    sum += score
  
  count = len(marks)
  
  return sum / count

marks = {'국어': 90, '영어': 80, '수학': 85}
average = get_average(marks)
print('평균은 {}점입니다.'.format(average))


total = 0

def gift(dic, who, money):
  dic[who] = money
  global total
  total += money

wedding = {}
gift(wedding, '영희', 5)
gift(wedding, '철수', 3)
gift(wedding, '이모', 10)
print('축의금 명단: {}'.format(wedding))
print('전체 축의금: {}'.format(total))