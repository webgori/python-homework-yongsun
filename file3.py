number = int(input('10 ~ 99 사이의 정수를 입력하세요 >>>'))
print(f'십의자리: {number // 10}')
print(f'일의자리: {number % 10}')

print('')

input_seconds = int(input('초를 입력하세요 >>>'))
hour = input_seconds // 60 // 60
minute = input_seconds // 60 % 60
seconds = input_seconds % 60

print(f'변환 결과는 {hour}시간 {minute}분 {seconds}초 입니다.')

print('')

employee_number = int(input('4자리 사원번호를 입력하세요 >>>'))
am_pm = '오전' if (employee_number % 10 >= 5) else '오후'
print(f'근무 시간은 {am_pm}입니다.')

print('')

max_ramen = 20
print(f'한 박스에 {max_ramen}개의 라면을 담을 수 있습니다.')
print('라면의 개수를 입력하시면 필요한 박스 수를 알려드립니다.')

ramens = int(input('라면의 개수를 입력하세요'))
box_count = (ramens // max_ramen) if (ramens % max_ramen == 0) else ((ramens // max_ramen) + 1)

print(f'{ramens}개 라면을 담으려면 {box_count}박스가 필요합니다.')

print('')

korean = int(input('국어 점수를 입력하세요 >>>'))
english = int(input('영어 점수를 입력하세요 >>>'))
math = int(input('수학 점수를 입력하세요'))

average = (korean + english + math) / 3
result = '합격' if (average >= 80) else '불합격'
print(f'평균은 {average}점이고, 결과는 {result}입니다.')