from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration, name='registration'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('hello_world/', views.hello_world, name='hello_world'),
]