from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.REGISTER, name='register'),
    path('login/', views.LOGIN, name='login'),
    path('logout/', views.LOGOUT, name='logout'),
]