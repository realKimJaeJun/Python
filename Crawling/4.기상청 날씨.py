"""
날짜 : 2023/01/16
이름 : 김재준
내용 : 파이썬 기상철 날씨 크롤링 실습하기
"""
import time
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pymysql

conn = pymysql.connect(host='127.0.0.1', 
                        user='root', 
                        password='1234', 
                        db='java2db', 
                        charset='utf8')
cur = conn.cursor()

# 가상 브라우저 실행
#chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)

#browser = webdriver.Chrome('./chromedriver.exe', options=chrome_options)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 페이지 이동
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

# 지역명 출력
trs = browser.find_elements(By.CSS_SELECTOR, '#weather_table > tbody > tr')
"""
for tr in trs:
    tds = tr.find_elements(By.CSS_SELECTOR, 'td')
    print('지역명 :', tds[0].text)
    print('현재일기 :', tds[1].text)
    print('시정km :', tds[2].text)
    print('운량1/10 :', tds[3].text)
    print('중하운량 :', tds[4].text)
    print('현재기온 :', tds[5].text)
    print('이슬점 온도 :', tds[6].text)
    print('체감온도 :', tds[7].text)
    print('일강수mm :', tds[8].text)
    print('적설cm :', tds[9].text)
    print('습도% :', tds[10].text)
    print('풍향 :', tds[11].text)
    print('풍속m/s :', tds[12].text)
    print('해면기압 :', tds[13].text)
"""
def f(index, x:str):
    if x == " ":return ""
    else : return f"`col{index}` = '{x}', "

def f2(tds):
    sql = "insert into `weather` set "
    for i in range(1, 14):
        sql += f(i, tds[i-1].text)
    sql += "`rdate` = NOW()"
    return sql

for tr in trs:
    tds = tr.find_elements(By.CSS_SELECTOR, 'td')

    # SQL 실행
    cur.execute(f2(tds))
    conn.commit()
    


# 가상 브라우저 종료
browser.close()