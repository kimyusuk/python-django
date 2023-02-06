from django.urls import path
from django.contrib.auth import views as auth_views

app_name='common'

urlpatterns = [
    #django.contrib.auth앱의 loginview 클래스를 활용할것
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login')
]
