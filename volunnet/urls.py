from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'volunnet'
urlpatterns = [
    path('activity_list', views.activity_list, name='activity_list'),
    path('register', views.register, name='register'),

]
