from django.contrib import admin
from django.urls import path 
from . import views


urlpatterns = [
    path('', views.Login_page , name='login'),
    path('login', views.Log , name='log'),
    path('dashboard' , views.dashboard , name='dashboard'),
    path('logout', views.Logout_request , name='logout' ),
    path('form', views.form , name='form' ),
    path('back',views.back,name='back'),
    path('lists', views.lists,name='list'),
    path('edit',views.infochg,name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
]