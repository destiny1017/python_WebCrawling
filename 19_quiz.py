from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.get("http://daum.net")

elem = browser.find_element_by_id("q")

elem.send_keys("송파 헬리오시티")
elem.send_keys(Keys.ENTER)

soup = BeautifulSoup(browser.page_source, "lxml")
trs = soup.find("div", attrs={"id":"estateCollTabContentsResult"}).find_all("tr")

for i, val in enumerate(trs):

    if i > 0:
        cols = val.find_all("div", attrs={"class":"txt_ac"})
        print(f"거래 : {cols[0].get_text()}")
        print(f"면적 : {cols[1].get_text()} (공급/전용)")
        print(f"가격 : {cols[2].get_text()} (만원)")
        print(f"동 : {cols[3].get_text()}")
        print(f"층 : {cols[4].get_text()}")
        print("-"*100)