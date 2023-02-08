#파일명 : urls.py
#설명:pybo의 모든 url과 view 함수의 맵핑을 담당

from django.urls import path
from .import views #현재 디랙터리에 views 모듈을 갖다 놓는 것이다.

app_name = 'pybo'

urlpatterns = [
    #base
    #index
    path('', views.index, name='index'),
    #path("<int:question_id>/", views.detail)
    path("<int:question_id>/", views.detail, name='detail'),#네임으로 맵핑

    #question
    path("question/create/", views.question_create, name='question_create'),
    path("question/modify/<int:question_id>/", views.question_modify, name="question_modify"), #수정폼
    path("question/delete/<int:question_id>/", views.question_delete, name="question_delete"), #삭제폼

    #answer
    path("answer/create/<int:question_id>/", views.answer_create, name='answer_create'),
    path("answer/modify/<int:answer_id>/", views.answer_modify, name='answer_modify'),
    path("answer/delete/<int:answer_id>/", views.answer_delete, name="answer_delete"),


    #temp menu
    path("boot/menu/", views.boot_menu, name="boot_menu"),
    #bootstrap template
    path("boot/list/", views.boot_list, name="boot_list"),
    path("boot/reg/", views.boot_reg, name="boot_reg"),
    #crawling
    path("crawling/cgv/", views.crawling_cgv, name="crawling_cgv"),
]
