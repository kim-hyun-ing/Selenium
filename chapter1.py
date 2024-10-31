from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
# import os
# os.system('pip install --upgrade selenium') #셀레니움 최신버전 설치

options = Options()
# options.add_argument("user-data-dir=C:\\파일 위치") #유저 데이터 저장(로그인 유지) 
# options.add_argument("disable-blink-features=AutomationControlled") #크롬 브라우저 자동화 탐지 비활성화(크롬 로그인 유지)
options.add_experimental_option("detach", True) #창 안 꺼지게
# options.add_experimental_option("excludeSwitches", ["enable-logging"]) #불필요한 메시지 출력X

driver = webdriver.Chrome(options=options) 
options.add_argument("--start-maximized") #창 전체화면

url = "https://naver.com"

driver.get(url)
time.sleep(3)

query = driver.find_element(By. ID, "query")
query.send_keys("입력하고 싶은 것")

# query.send_keys(Keys.ENTER)  #1 엔터 누르는 버전

search_btn = driver.find_element(By.CSS_SELECTOR, "#search-btn")  #2 검색버튼 누르는 버전
search_btn.click()

# driver.save_screenshot("naver_test.png")

driver.quit()