from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = 'volunnet'
urlpatterns = [

    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),

    path('activity_list', views.activity_list, name='activity_list'),
    path('activity_new', views.activity_new, name='activity_new'),

    path('register/', views.register, name='register'),

]
