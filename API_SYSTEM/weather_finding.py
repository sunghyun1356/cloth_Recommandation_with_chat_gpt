#import 해주기
from bs4 import BeautifulSoup
import urllib.request
import requests
import re

import numpy as np
# 날씨 정보 parsing해주기





def show():
    url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

    result ={}
#위치, 최저/최고/현재 온도, 습도, 미세먼지, 강수 정보 추출
    result['location'] = soup.select_one('div.title_area._area_panel > h2.title').text.strip()

    temp_text = soup.select_one('div.temperature_text > strong').text
    result['temperature'] = float(''.join(a for a in temp_text if a.isdecimal() or a =='.'))

    highest_temp_str =soup.find('span', class_='highest').text.strip()
    result['final_highest'] = int(''.join(c for c in highest_temp_str if c.isdecimal()))

    lowest_temp_str = soup.find('span', class_='lowest').text.strip()
    result['final_lowest'] = int(''.join( a for a in lowest_temp_str if a.isdecimal()))

    item= soup.select('div.temperature_info > dl.summary_list > div.sort')[1]
    result['humidity'] = item.select_one('dd.desc').text.strip()


    result['fine_dust'] = soup.select_one('div.report_card_wrap > ul.today_chart_list > li.item_today.level2 > a > span.txt').text.strip()

    result['precipitation'] = soup.select_one('div.temperature_info > p.summary > span.weather.before_slash').text
    command = (
        f'스타일을 추천 받고 싶습니다.\n\n'
        f'이곳은 {result["location"]}이며\n'
        f'날씨는 {result["temperature"]}입니다.\n'
        f'최저기온은 {result["final_lowest"]}도, '
        f'최고기온은 {result["final_highest"]}도이며\n'
        f'미세먼지 농도는 {result["fine_dust"]},\n'
        f'오늘의 강수는 {result["precipitation"]}이며\n'
        f'오늘의 습도는 {result["humidity"]}입니다.\n'
        )
    return command