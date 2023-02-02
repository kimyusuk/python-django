from django.test import TestCase
import unittest
import datetime
import logging
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
class Crawling(unittest.TestCase):
    def setup(self):
        print("setUp")
    def test_naver_stock(self):
        codes = {"삼성전자":"005930","현대차":"005380"}
        for i in codes.keys():
            url = "https://finance.naver.com/item/main.naver?code="
            urlc = url + str(codes[i])
            response = requests.get(urlc)
            if 200 == response.status_code:
                html = response.text
                bs4 = BeautifulSoup(html, "html.parser")
                price = bs4.select("div.today p.no_today span.blind")
                print("종목명: {},코드: {},주가: {}".format(i,codes[i],price[0].getText()))
            else:
                print("접속 오류")


    @unittest.skip("테스트 연습")
    def tearDown(self):
        print("tearDown")
    @unittest.skip("테스트 연습")
    def call_slemdunk(self,url):
        # url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=223800&target=after&page=1"
        response = requests.get(url)
        if 200 == response.status_code:
            html = response.text
            bs4 = BeautifulSoup(html, "html.parser")
            score = bs4.select("div.list_netizen_score em")
            review = bs4.select("table tbody tr td.title")
            for i in range(0,len(score)):
                review_text = review[i].getText().split('\n')
                if len(review_text)>2:
                    tmp_text = review_text[5]
                else:
                    tmp_text = review_text[0]
                print("평점 감상평:{}, {}".format(score[i].getText(),tmp_text))
    @unittest.skip("테스트 연습")
    def test_slemdunk(self):
        url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=223800&target=after&page=1"
        for i in range(1, 4, 1):
            self.call_slemdunk(url + str(i))
    @unittest.skip("테스트 연습")
    def test_cgv(self):
        #cgv = http://www.cgv.co.kr/movies/?lt=1&ft=0
        url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"
        response = requests.get(url)
        print(response.status_code)
        if 200 == response.status_code:
            html = response.text
            bs4 = BeautifulSoup(html, "html.parser")
            title = bs4.select("div.box-contents strong.title")
            reserve = bs4.select("div.score strong.percent span")
            poster = bs4.select("span.thumb-image img")
            for i in range(0,7,1):
                posterImg = poster[i]
                imgUrlPath = posterImg.get('src')
                # print(imgUrlPath)
                print("영화:{}, {}, {}".format(title[i].getText(),reserve[i].getText(),imgUrlPath))
        else:
            print("접속오류 response.status_code:{}".format(response.status_code))
    @unittest.skip("테스트 연습")
    def test_weather(self):
        #날씨 = https://weather.naver.com/today/02113132?cpName=KMA
        now = datetime.datetime.now()
        #yyyymmdd hh:mm
        newDate = now.strftime("%Y-%m-%d %H:%M:%S")
        print("="*35)
        print(newDate)
        print("=" * 35)
        naverWeatherUrl ="https://weather.naver.com/today/09545101"
        html = urlopen(str(naverWeatherUrl))
        print(html)
        bsObj = BeautifulSoup(html, "html.parser")
        temps = bsObj.find('strong', 'current')
        print("서울 마포구 서교동 날씨:{}".format(temps.getText()))
