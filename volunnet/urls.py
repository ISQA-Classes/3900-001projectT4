from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views


app_name = 'volunnet'
urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.user_login, name ='user_login'),
    path('logout/', views.logoutUser, name='logout'),
    re_path(r'^home/$', views.home, name ='home'),
    path('activity_list', views.search, name='activity_list'),
    path('activity_new', views.activity_new, name='activity_new'),
    path('activity/<int:pk>/edit/', views.activity_edit, name='activity_edit'),
    path('activity/<int:pk>/delete/', views.activity_delete, name='activity_delete'),
    path('register/', views.register, name='register'),
    path('activity_list', views.activity_list, name='activity_list'),
    path('register', views.register, name='register'),
    path('signupas', views.signupas, name='signupas'),
    path('OrganizationRegistration/', views.OrganizationRegister, name='OrganizationRegister'),

    path('vol_list', views.vol_list, name='vol_list'),
    path('apply/', views.apply, name='apply'),
    #added by CV
<<<<<<< HEAD
    path('volunteer_list', views.search, name='volunteer_list'),

=======
    #path('volunteer_list', views.search, name='volunteer_list'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
>>>>>>> 8d694cea8f00b6d82fce10575e90992129885b3e
]
