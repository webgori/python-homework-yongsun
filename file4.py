score = int(input('점수를 입력하세요 >>>'))

if score >= 90:
  print(f'점수는 {score}점이고, 학점은 A학점입니다.')
elif score >= 80:
  print(f'점수는 {score}점이고, 학점은 B학점입니다.')
elif score >= 70:
  print(f'점수는 {score}점이고, 학점은 C학점입니다.')
elif score >= 60:
  print(f'점수는 {score}점이고, 학점은 D학점입니다.')
else:
  print(f'점수는 {score}점이고, 학점은 F학점입니다.')
  
decimal = int(input('정수를 입력하세요 >>>'))

if decimal % 3 == 0:
  print(f'{decimal}는 3의 배수입니다.')
else:
  print(f'{decimal}는 3의 배수가 아닙니다.')
  
decimal1 = int(input('정수1 입력 >>>'))
decimal2 = int(input('정수2 입력 >>>'))
decimal3 = int(input('정수3 입력 >>>'))

if decimal1 >= decimal2 and decimal1 >= decimal3:
  print(f'가장 큰 수는 {decimal1} 입니다.')
elif decimal2 >= decimal1 and decimal2 >= decimal3:
  print(f'가장 큰 수는 {decimal2} 입니다.')
elif decimal3 >= decimal1 and decimal3 >= decimal2:
  print(f'가장 큰 수는 {decimal3} 입니다.')
  
car_number = input('차량번호를 입력하세요 >>>')
#last_car_number = int(car_number[-2])
last_car_number = int(car_number[8:9])

if last_car_number % 2 == 0:
  print(f'차량번호 {car_number}는 오늘 운행가능입니다.')
else:
  print(f'차량번호 {car_number}는 오늘 운행불가능입니다.')