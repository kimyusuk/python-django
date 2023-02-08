import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
#ctrl + alt + o = 안쓰는 import 삭제 + 정리

def boot_menu(request):
    return render(request, "pybo/menu.html")

def boot_list(request):
    return render(request, "pybo/list.html")

def boot_reg(request):
    return render(request, "pybo/reg.html")

def crawling_cgv(request):
    url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"
    response = requests.get(url)
    print(response.status_code)
    context = {}
    if 200 == response.status_code:
        html = response.text
        bs4 = BeautifulSoup(html, "html.parser")
        title = bs4.select("div.box-contents strong.title")
        reserve = bs4.select("div.score strong.percent span")
        poster = bs4.select("span.thumb-image img")
        title_list = []
        reserve_list = []
        poster_list = []
        for i in range(0,7,1):
            posterImg = poster[i]
            imgUrlPath = posterImg.get('src')
            title_list.append(title[i].getText()) #제목
            reserve_list.append(reserve[i].getText()) #예매율
            poster_list.append(imgUrlPath) #포스터 소스
            print("영화:{}, {}, {}".format(title[i].getText(),reserve[i].getText(),imgUrlPath))
        context = {"context": zip(title_list, reserve_list, poster_list)}
    else:
        print("접속오류 response.status_code:{}".format(response.status_code))

    return render(request, "pybo/crawling_cgv.html", context)