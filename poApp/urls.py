from django.urls import path
from poApp import views

urlpatterns = [
    path('insert', views.insert,name='insert'),
    path('insertdata', views.insert_data),
    path('display', views.display_fun, name='display'),
    path('updatedata/<int:id>', views.update_fun, name='updatedata'),
    path('deletedata/<int:id>', views.delete_fun, name='deletedata'),
    path('navbar', views.navbar),
    path('index', views.index,name='index'),

]