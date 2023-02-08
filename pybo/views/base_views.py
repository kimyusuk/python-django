import logging
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from ..models import Question
#ctrl + alt + o = 안쓰는 import 삭제 + 정리

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

def detail(request,question_id):
    #question 상세
    logging.info('1. question_id:{}'.format(question_id))
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question,pk=question_id) # 오류 화면 구현 + 데이터베이스 불러오기
    logging.info('2. question:{}'.format(question))
    context = {"question": question}
    return render(request, 'pybo/question_detail.html', context)