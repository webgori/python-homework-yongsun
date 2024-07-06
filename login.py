# pip install selenium

# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time

from selenium.webdriver.common.by import By

# 크롬드라이버 실행
driver = webdriver.Chrome()

#크롬 드라이버에 url 주소 넣고 실행
driver.get('https://practicetestautomation.com/practice-test-login/')

# 페이지가 완전히 로딩되도록 3초동안 기다림
driver.implicitly_wait(3)

username = 'student'
driver.find_element(By.ID, 'username').send_keys(f'{username}')

time.sleep(1)

password = 'Password123'
driver.find_element(By.ID, 'password').send_keys(f'{password}')

time.sleep(1)

driver.find_element(By.ID, 'submit').click()

driver.implicitly_wait(3)

# 화면캡처
driver.get_screenshot_as_file('capture_login.png')

time.sleep(3)