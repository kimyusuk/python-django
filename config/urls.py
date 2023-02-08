"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from pybo.models import Question,Answer
# from django.utils import timezone
# q=Question(subject="파이썬 게시판은 무엇인가요?",content="알고 싶어요!",create_date=timezone.now())
# q=Question(subject="장고 모델은 무엇인가요?",content="id는 자동으로 생성되나요!",create_date=timezone.now())
# q.save()
#데이터 모두 추출
# Question.objects.all()
# q = Question.objects.get(id=2)
# q
# q.subject = 'Django Model Question'
# q = Question.objects.get(id=3)
# q.delete()
# q = Question.objects.get(id=1)
# a = Answer(question=q,content='id는 자동생성 됩니다.',create_date=timezone.now())
# a.save()
# a = Answer.objects.get(id=1)
# a.question
# q.answer_set.all()
from django.contrib import admin
from django.urls import path, include
from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),
]
