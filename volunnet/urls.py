from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.contrib.auth import logout

app_name = 'volunnet'
urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.user_login, name ='user_login'),
    path('logout/', views.logoutUser, name='logout'),
    re_path(r'^home/$', views.home, name ='home'),
    path('activity_list', views.activity_list, name='activity_list'),
    path('activity_new', views.activity_new, name='activity_new'),
    path('activity/<int:pk>/edit/', views.activity_edit, name='activity_edit'),
    path('activity/<int:pk>/delete/', views.activity_delete, name='activity_delete'),
    path('register/', views.register, name='register'),
    path('activity_list', views.activity_list, name='activity_list'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('signupas', views.signupas, name='signupas'),
    path('OrganizationRegistration/', views.OrganizationRegister, name='OrganizationRegister')
]
