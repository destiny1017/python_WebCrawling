import requests
import re
from bs4 import BeautifulSoup

for i in range(1, 6):
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}
    # url = "https://www.google.com"
    res = requests.get(url, headers=headers);
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    # print(items[0].find("div", attrs={"class":"name"}).get_text())

    for item in items:

        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            # print(" -광고상품 제외-")
            # print("======================================")
            continue

        name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
        price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격
        rate = item.find("em", attrs={"class":"rating"}) # 평점
        rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) # 평점 수
        link = "https://www.coupang.com"
        link += item.find("a", attrs={"class":"search-product-link"})["href"] #링크
        if "레노버" in name:
            # print(" - 레노버 상품 제외 - ")
            # print("======================================")
            continue
        if rate:
            rate = rate.get_text()
            rate_cnt = rate_cnt.get_text()
            rate_cnt = rate_cnt[1:-1]
        else:
            rate = "평점 없음"
            rate_cnt = "평점 없음"
            # print(" -평점 없는 상품 제외-")
            # print("======================================")
            continue

        if float(rate) >= 5.0 and int(rate_cnt) >= 500:
            print(f"상품명:", name)
            print(f"가격:", price)
            print(f"평점: {rate}점 ({rate_cnt})개")
            print(f"링크:", link)
            print("======================================")
