from random import shuffle
from time import sleep

pot = list(range(1, 46))
jackpot = []

for i in range(1, 7):
  shuffle(pot)
  last_number = pot.pop()
  print(f'{i}번째 당첨번호는 {last_number} 입니다.')
  jackpot.append(last_number)
  sleep(2)
  
jackpot.sort()
print(f'이번 당첨번호는 {jackpot} 입니다.')



from random import randint
from datetime import datetime
from math import floor

# 211p
random_value = randint(1, 100)
start_datetime = datetime.now()

while True:
  answer = int(input('어떤 값일까요? >>>'))
  
  if random_value > answer:
    print('Up')
  elif random_value < answer:
    print('Down')
  else:
    print('정답입니다.')
    break

# 215p
end_datetime = datetime.now()
datetime_diff = end_datetime - start_datetime

# 217p
total_seconds = datetime_diff.total_seconds()
# 210p
total_seconds = floor(total_seconds)

print(f'{total_seconds}초 만에 성공했습니다.')






'''
1에서 45 사이의 모든 정수를..
 1. list와 range(1, 46) 사용하는 방법
 2. for와 range(1, 46) 사용하는 방법

pot 리스트를 무작위로 섞어줍니다
 212p shuffle() 함수 참고

pot 리스트의 마지막 숫자 하나를 빼서...
 175p pop() 메소드 참고

2초 동안 잠시 멈춥니다.
 215p sleep() 함수 참고

jackpot 리스트의 모든 요소를 오름차순 정렬합니다.
 jackpot.sort()

1번째 당첨번호는 38입니다.
2초쉬고
2번째 당첨번호는 42입니다.
2초쉬고
'''





'''
1에서 100 사이의 정ㅇ수 중 하나를 임의로 생성
 211p randint 함수 사용

정답을 맞히면 몇 초 만에 정답을 맞혔는지 출력
 반복문 시작 전에 215p datetime.now() 함수 사용
 반복문 종료 후에 215p datetime.now() 함수 사용
 반복문 시작 전 datetime - 반복문 종료 후 datetime 한 후 217p의 total_seconds() 메서드 사용
 
소수 아래 값은 내림 처리
 210p floor 함수 사용
'''