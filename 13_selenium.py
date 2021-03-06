# 크롬드라이버 설치
# pip install selenium
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://naver.com")

elem = browser.find_element_by_class_name("link_login") # link_login 클래스를 가진 엘리먼트 가져오기(로그인)
elem.click() # 해당 엘리먼트에 클릭 동작

browser.back() # 뒤로가기
browser.forward() # 앞으로가기
browser.refresh() # 새로고침

elem = browser.find_element_by_id("query") # 검색창 찾기

from selenium.webdriver.common.keys import Keys # keys 사용을 위해 import

elem.send_keys("나도코딩") # 검색창에 입력
elem.send_keys(Keys.ENTER) # 검색창에서 엔터명령

elem = browser.find_elements_by_tag_name("a") # browser에서 a 태그인 모든 element 찾기

for e in elem:
    e.get_attribute("href") # 찾아온 모든 a 태그의 href 속성 출력



browser.get("http://daum.net")
elem = browser.find_element_by_name("q")

elem.send_keys("나도코딩")
elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
elem.click()