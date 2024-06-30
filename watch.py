class Watch():
    def set_time(self, time):
        self.hour = int(time[0:2])
        self.minute = int(time[3:5])
        self.second = int(time[6:8])
    
    def add_hour(self, hour):
        self.hour += hour

    def add_minute(self, minute):
        self.minute += minute

        # 분으로 시간을 구하는 공식
        # 분 / 60 = 몫이 시간, 나머지가 분
        hour = self.minute // 60
        self.hour += hour

        self.minute = self.minute % 60


    def add_second(self, second):
        self.second += second

        # 초로 분을 구하는 공식
        # 초 / 60 = 몫이 분, 나머지가 초
        minute = self.second // 60
        self.minute += minute

        self.second = self.second % 60

    def print_calc_time(self):
        print(f'계산된 시간은 {self.hour}시 {self.minute}분 {self.second}초')
        

watch = Watch()

time = input('시간을 입력하세요 >>>')
watch.set_time(time)

hour = int(input('계산할 시간을 입력하세요 >>>'))
minute = int(input('계산할 분을 입력하세요 >>>'))
second = int(input('계산할 초를 입력하세요 >>>'))

watch.add_second(second)
watch.add_minute(minute)
watch.add_hour(hour)

watch.print_calc_time()