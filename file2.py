first_number_input = float(input('첫 번째 실수를 입력하세요 >>>'))
second_number_input = float(input('두 번째 실수를 입력하세요 >>>'))
sum = first_number_input + second_number_input
print(f'{first_number_input}와 {second_number_input}의 합은 {sum}입니다.')

last_day_of_the_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_input = int(input('1~12 사이의 월을 입력하세요 >>>'))
print(f'{month_input}월은 {last_day_of_the_month[month_input - 1]}일까지 있습니다.')

english_dict = {'flower':'꽃','fly':'날다','floor':'바닥'}
english_word_input = input('영어 단어를 입력하세요 >>>')
print(f'{english_word_input}: {english_dict[english_word_input]}')

trip_places = set()
trip1_input = input('희망하는 수학여행지를 입력하세요 >>>')
trip_places.add(trip1_input)

trip2_input = input('희망하는 수학여행지를 입력하세요 >>>')
trip_places.add(trip2_input)

trip3_input = input('희망하는 수학여행지를 입력하세요 >>>')
trip_places.add(trip3_input)

print(f'조사된 수학여행지는 {trip_places}입니다.')