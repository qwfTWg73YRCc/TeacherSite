# from django.urls import path
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'', views.MainPage, name="mainpage"),
    url(r'about', views.About, name="about"),
]

urlpatterns += staticfiles_urlpatterns()
