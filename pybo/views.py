from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import  Question
from django.utils import timezone
from .forms import QuestionForm


def boot_menu(request):
    return render(request, "pybo/menu.html")
def index(request):
    # return HttpResponse("Hello pybo에 안녕하세요.pybo")
    # list order create_date desc
    # order_by('-필드') = desc,order_by('필드') = asc
    question_list = Question.objects.order_by("-create_date")
    # question_list = Question.objects.filter(id=1)
    context = {"question_list":question_list} # list order creat_date desc
    # print("question_list:{}".format(question_list))
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
    print('1. question_id:{}'.format(question_id))
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question,pk=question_id) # 오류 화면 구현 + 데이터베이스 불러오기
    print('2. question:{}'.format(question))
    context = {"question": question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    print('answer_create:{}'.format(question_id))
    question = get_object_or_404(Question,pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail',question_id=question.id)

def boot_list(request):
    return render(request, "pybo/list.html")

def boot_reg(request):
    return render(request, "pybo/reg.html")
