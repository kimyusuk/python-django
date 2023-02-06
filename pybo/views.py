from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import  Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
import logging
from bs4 import BeautifulSoup
import requests
from django.core.paginator import Paginator


def boot_menu(request):
    return render(request, "pybo/menu.html")
def index(request):
    # return HttpResponse("Hello pybo에 안녕하세요.pybo")
    # list order create_date desc
    # order_by('-필드') = desc,order_by('필드') = asc
    logging.info("index 레벨로 출력")
    # print("index 레벨로 출력")
    page = request.GET.get('page','1')
    logging.info("page:{}".format(page))
    question_list = Question.objects.order_by("-create_date")
    paginator = Paginator(question_list,10)
    pageObj = paginator.get_page(page)
    # paginator.count: 전체 게시물 갯수
    # paginator.per_page: 페이지당 보여줄 게시물 갯수
    # paginator.page_range: 페이지범위
    # number: 현재페이지 번호
    # previous_page_number: 이전 페이지 번호
    # next_page_number: 다음 페이지 번호
    # has_previous: 이전 페이지 유무
    # has_next: 다음 페이지 유무
    # start_index: 현재 페이지 시작 인덱스(1부터 시작)
    # end_index: 현재 페이지 끝 인덱스
    # question_list = Question.objects.filter(id=1)
    context = {"question_list" : pageObj} # list order creat_date desc
    logging.info("pageObjValue:{}".format(pageObj))
    return render (request,'pybo/question_list.html',context)

def question_create(request):
    if request.method == "POST":
        #저장
        form = QuestionForm(request.POST) # request.Post 데이터
        if form.is_valid(): #form이 유효하면
            question = form.save(commit=False) # create_date 없기 때문에 db에 확정은 안함
            question.create_date = timezone.now()
            question.save() #날짜 추가 생성 저장
            return redirect("pybo:index")
    else:                               
        form = QuestionForm()            #get 데이터
    context = {"form" : form}
    return render(request, "pybo/question_form.html", context)

def detail(request,question_id):
    #question 상세
    logging.info('1. question_id:{}'.format(question_id))
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question,pk=question_id) # 오류 화면 구현 + 데이터베이스 불러오기
    logging.info('2. question:{}'.format(question))
    context = {"question": question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question,pk=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect("pybo:detail", question_id = question.id)
    else:
        return HttpResponseNotAllowed("Post만 가능 합니다.")

    #form validation
    context = { "question" : question, "form" : form }
    return render(request, "pybo/question_detail.html", context)
    
    #수정
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # return redirect('pybo:detail',question_id=question.id)

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