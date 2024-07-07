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
login_url = 'https://naver.com'
driver.get(login_url)

# 페이지가 완전히 로딩되도록 3초동안 기다림
driver.implicitly_wait(3)

# 사용자 이름
keyword = 'flower'
# id가 username인 요소에 사용자 이름을 입력
#driver.find_element(By.CSS_SELECTOR, "textarea[label='검색']").send_keys(f'{keyword}')
driver.find_element(By.ID, 'query').send_keys(f'{keyword}')

# 1초 딜레이
time.sleep(1)

driver.find_element(By.CLASS_NAME, 'btn_search').click()

time.sleep(5)

# 화면캡처
# driver.get_screenshot_as_file('capture_login.png')

# 종료 전 3초 딜레이
# time.sleep(3)