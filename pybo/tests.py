from django.test import TestCase
import unittest
import datetime
import logging
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pyperclip
from selenium.webdriver.common.keys import Keys




class Crawling(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='C:\BIG_AI0102\PYTHON_01_BASIC\app\geckodriver.exe')
        logging.info("setUp")

    def tearDown(self):
        logging.info("teardown")
        #self.browser.quit()

    @unittest.skip("테스트 연습")
    def test_clipboard_naver(self): #ctrl c,v 우회
        self.browser.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
        user_id = "airheart0422"
        user_pw = "qkqh0718@"

        #id
        id_textinput = self.browser.find_element(By.ID,'id')
        id_textinput.click()
        #클립보드로 copy
        pyperclip.copy(user_id)
        id_textinput.send_keys(Keys.CONTROL,'v')
        time.sleep(1)

        #password
        pw_textinput = self.browser.find_element(By.ID,'pw')
        pw_textinput.click()
        pyperclip.copy(user_pw)
        pw_textinput.send_keys(Keys.CONTROL,'v')
        time.sleep(1)

        btn_login = self.browser.find_element(By.ID,'log.login')
        btn_login.click()
    @unittest.skip("테스트 연습")
    def test_naver(self):
        self.browser.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
        print("browser:{}".format(self.browser))
        id_textarea = self.browser.find_element(By.ID, 'id')
        id_textarea.send_keys('airheart0422')
        pw_textarea2 = self.browser.find_element(By.ID, 'pw')
        pw_textarea2.send_keys('qkqh0718@')
        btn = self.browser.find_element(By.ID, 'log.login')
        btn.click()
    @unittest.skip("테스트 연습")
    def test_selenium(self):
        #firefox로 웹 드라이버 객체에게 get을 통하여 네이버의 http요청을 하게 함.
        self.browser.get('http://192.168.219.103:8000/pybo/503/')
        print("self.browser:{}".format(self.browser.title))
        self.assertIn('Pybo',self.browser.title)
        content_textarea = self.browser.find_element(By.ID,'content')
        content_textarea.send_keys('나는 귀염둥이다!')
        btn = self.browser.find_element(By.ID,'submit_btn')
        btn.click()
    @unittest.skip("테스트 연습")
    def test_zip(self):
        integer = [1,2,3]
        letters = ['a','b','c']
        floats = [4.0, 8.0, 10.0]
        zipped = zip(integer,letters,floats)
        list_data = list(zipped)
        # for i in zipped:
        #     print(i)#(1, 'a', 4.0) (2, 'b', 8.0) (3, 'c', 10.0)
        # for i in list_data:
        #     print(i)#(1, 'a', 4.0) (2, 'b', 8.0) (3, 'c', 10.0)
        print("list_data:{}".format(list_data))
    @unittest.skip("테스트 연습")
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
