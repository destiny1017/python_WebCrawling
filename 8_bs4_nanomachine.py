import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=747271&weekday=thu"
headers = {}
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs={"class": "title"})
title = cartoons[1].a.get_text()
link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com" + link)

# # 각 회당 url추출하기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# 평점 구하기

# stars = soup.find_all("span", attrs={"class":"star"})
# for star in stars:
#     starRank = star.find_next_sibling("strong")
#     print(, starRank.get_text())


# stars = soup.find_all("span", attrs={"class":"star"})
print("##평점##")
averageRank = 0;
for cartoon in cartoons:
    star = cartoon.find_next_sibling("td")
    starRank = star.find("strong").get_text()
    # starRank = star.get_text()
    print(cartoon.a.get_text(), " : ", starRank)
    averageRank += float(starRank)

# print("평균 평점: {4}".format(averageRank / len(cartoons)))
# print("평균 평점: {0:.2f}".format(averageRank / len(cartoons)))
print("평균 평점: %.2f" % (averageRank / len(cartoons)))

