from django.urls import path

from LoginApp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('log',views.log,name='log'),
    path('reg',views.reg,name='reg'),

    path('readreg',views.read_reg),
    path('readlog',views.read_log),
    path('logout',views.read_logout,name='logout'),
]