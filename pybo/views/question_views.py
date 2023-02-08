from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ..forms import QuestionForm
from ..models import Question

#ctrl + alt + o = 안쓰는 import 삭제 + 정리
@login_required(login_url='common:login') # 로그인 되어있지 않으면 login페이지로 이동
def question_create(request):
    if request.method == "POST":
        #저장
        form = QuestionForm(request.POST) # request.Post 데이터
        if form.is_valid(): #form이 유효하면
            question = form.save(commit=False) # create_date 없기 때문에 db에 확정은 안함
            question.create_date = timezone.now()
            question.author = request.user
            question.save() #날짜 추가 생성 저장
            return redirect("pybo:index")
    else:
        form = QuestionForm()            #get 데이터
    context = {"form" : form}
    return render(request, "pybo/question_form.html", context)

@login_required(login_url='common:login')
def question_modify(request,question_id):
    # 질문 수정
    question = get_object_or_404(Question, pk=question_id) #question id로 Question 조회

    #권한 check
    if request.user != question.author: #현 사용자와 글쓴이가 맞질 않으면
        messages.error(request, "수정 권한이 없습니다.")
        return redirect('pybo:detail', question_id = question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)

        if form.is_valid():
            question = form.save(commit=False) #수정일시 없이 저장한다. 그니까 더 저장할것이니까 False
            question.modify_date = timezone.now() #수정일시 저장
            question.save() #최종저장
            return redirect("pybo:detail", question_id = question.id)
    else:
        form = QuestionForm(instance=question) # get 수정 데이타
    context = {'form':form}
    return render(request, "pybo/question_form.html", context)

@login_required(login_url='common:login')
def question_delete(request,question_id):
    question = get_object_or_404(Question,pk=question_id)

    if request.user != question.author:
        messages.error("삭제권한이 없습니다.")
        return redirect("pybo:detail",question_id=question.id)

    question.delete() #삭제
    return redirect("pybo:index")