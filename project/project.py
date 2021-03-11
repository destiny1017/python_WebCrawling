import requests
from bs4 import BeautifulSoup


def today_weather():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98+%EB%82%A0%EC%94%A8"
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    cast_txt = soup.find("p", attrs={"class": "cast_txt"})
    today_temp = soup.find("span", attrs={"class": "todaytemp"})
    prob_rain = soup.find("li", attrs={"class": "date_info today"}).find_all("span", attrs={"class": "num"})
    dust = soup.find("dl", attrs={"class": "indicator"}).find_all("dd")
    low_high_temp = soup.find("span", attrs={"class": "merge"}).get_text().split("/")

    print("[오늘의 날씨]")
    print(cast_txt.get_text())
    print(f"현재 {today_temp.get_text()}℃ (최저 {low_high_temp[0]} / 최고 {low_high_temp[1]})")
    print(f"오전 강수확률 {prob_rain[0].get_text()}% / 오후 강수확률 {prob_rain[1].get_text()}%")
    print("")
    print("미세먼지", dust[0].get_text())
    print("초미세먼지", dust[1].get_text())


def headline_news():
    url = "https://news.naver.com/main/home.nhn"
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    articles = soup.find_all("a", attrs={"class": "lnk_hdline_article"})

    print("\n[헤드라인 뉴스]")
    for i, article in enumerate(articles):
        title = article.get_text()
        link = "https://news.naver.com/" + article["href"]
        print(f"{i+1}. {title.strip()} \n({link})")
        if i == 2:
            break

    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    articles_it = soup.find("ul", attrs={"class": "type06_headline"}).find_all("li")

    print("\n[IT일반 뉴스]")
    for i, article in enumerate(articles_it):
        title = article.a.img["alt"]
        link = article.a["href"]
        print(f"{i+1}. {title} \n({link})")
        if i == 2:
            break


if __name__ == "__main__":
    today_weather()
    headline_news()
