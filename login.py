# pip install selenium

# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver

# 딜레이에 사용할 time 모듈 import
import time

# 요소에 접근할 수 있는 By 함수 import
from selenium.webdriver.common.by import By

# 크롬드라이버 실행
driver = webdriver.Chrome()

#크롬 드라이버에 url 주소 넣고 실행
login_url = 'https://practicetestautomation.com/practice-test-login'
driver.get(login_url)

# 페이지가 완전히 로딩되도록 3초동안 기다림
driver.implicitly_wait(3)

# 사용자 이름
username = 'student'
# id가 username인 요소에 사용자 이름을 입력
driver.find_element(By.ID, 'username').send_keys(f'{username}')

# 1초 딜레이
time.sleep(1)

# 비밀번호
password = 'Password123'
# id가 password인 요소에 비밀번호 입력
driver.find_element(By.ID, 'password').send_keys(f'{password}')

# 1초 딜레이
time.sleep(1)

# id가 submit인 요소를 클릭
driver.find_element(By.ID, 'submit').click()

# 페이지 로딩까지 3초 기다림
driver.implicitly_wait(3)

# 화면캡처
driver.get_screenshot_as_file('capture_login.png')

# 종료 전 3초 딜레이
time.sleep(3)