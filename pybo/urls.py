#파일명 : urls.py
#설명:pybo의 모든 url과 view 함수의 맵핑을 담당

from django.urls import path
from .import views #현재 디랙터리에 views 모듈을 갖다 놓는 것이다.

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    #path("<int:question_id>/", views.detail)
    path("<int:question_id>/", views.detail, name='detail'),#네임으로 맵핑
    path("answer/create/<int:question_id>", views.answer_create, name='answer_create'),
    path("question/create/", views.question_create, name='question_create'),

    #temp menu
    path("boot/menu/", views.boot_menu, name="boot_menu"),
    #bootstrap template
    path("boot/list/", views.boot_list, name="boot_list"),
    path("boot/reg/", views.boot_reg, name="boot_reg"),

    #crawling
    path("crawling/cgv/", views.crawling_cgv, name="crawling_cgv")
]
