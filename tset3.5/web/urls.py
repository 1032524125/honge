from django.conf.urls import url

from app import views

urlpatterns = [
    #进入前端登录页面
    url(r'^loginw/',views.loginw,name='loginw')
]