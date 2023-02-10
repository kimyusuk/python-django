import logging
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone
from ..forms import AnswerForm
from ..models import Question, Answer
#ctrl + alt + o = 안쓰는 import 삭제 + 정리

@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect("{}#answer_{}".format(resolve_url('pybo:detail', question_id=question.id),answer.id))
    else:
        form = AnswerForm()
    # form validation
    context = {"question": question, "form": form}
    return render(request, "pybo/question_detail.html", context)
    # 수정
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # return redirect('pybo:detail',question_id=question.id)

@login_required(login_url='common:login')
def answer_modify(request,answer_id):
    logging.info("1.answer_modify:{}".format(answer_id))
    #1.answer id에 해당되는 데이터 조회
    #2.수정권한 체크 : 권한이 없는 경우 메시지 전달
    #3. POST: 수정
    #4. GET: 수정 Form 전달

    #1.
    answer = get_object_or_404(Answer, pk=answer_id)
    #2.
    if request.user != answer.author:
        messages.error(request,'수정 권한이 없습니다.')
        return redirect("pybo:detail", question_id = answer.question.id)
    #3.
    if request.method == "POST": #수정
        form = AnswerForm(request.POST, instance=answer) #instatnce = parameter
        logging.info("2.answer_modify:{}".format(answer))

        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            logging.info("3.answer_modify POST form.isvalid():{}".format(answer))
            answer.save()
            return redirect("{}#answer_{}".format(resolve_url('pybo:detail', question_id=answer.question.id), answer.id))
    else:                        #수정 form의 tempalte
        form = AnswerForm(instance=answer)  # get 수정 데이타
    context = {"answer":answer, 'form': form}
    return render(request, "pybo/answer_form.html", context)

@login_required(login_url='common:login')
def answer_delete(request,answer_id):
    logging.info('1.answer_delete:{}'.format(answer_id))
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user != answer.author:
        messages.error("삭제권한이 없습니다.")
        return redirect("pybo:detail", question_id = answer.question.id)

    answer.delete() #삭제
    return redirect("pybo:index")

@login_required(login_url='common:login')
def answer_vote(request,answer_id):
    logging.info('1.answer_voter:{}'.format(answer_id))
    answer = get_object_or_404(Answer, pk=answer_id)

    #본인 글은 본인이 추천 못하게
    if request.user == answer.author:
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다.")
    else:
        answer.voter.add(request.user)
    return redirect("{}#answer_{}".format(resolve_url('pybo:detail', question_id=answer.question.id), answer.id))
